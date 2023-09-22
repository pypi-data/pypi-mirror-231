import json
import os
from datetime import datetime, timedelta
from typing import List

import requests
from celery import shared_task
from django.conf import settings
from sat.db import ConnectionType, SatDBException, get_db_connection
from sat.logs import SATLogger
from sat.slack import Slack

from sat_automations.gold_feed_automation.config import (
    CCURE_CONNECTION,
    FEED_CONNECTION,
    FEED_INSERT_QUERY,
    GOLD_CONNECTION,
    GOLD_PRTG_URL,
)
from sat_automations.gold_feed_automation.helper_queries import (
    return_ccure_user_query,
    return_gold_user_query,
)
from sat_automations.gold_feed_automation.models import CCureUser, GoldUser
from sat_automations.utils.authenticate import GoogleAuthenticate

logger = SATLogger(__name__)

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
slack = Slack(os.getenv("SLACK_BOT_TOKEN"))


class GoldCredentialFeed:
    def __init__(self) -> None:
        self.authenticator = GoogleAuthenticate("gold_credential_feed")
        self.authenticator.authenticate()
        if self.authenticator.response_json:
            self.access_token = self.authenticator.response_json.get("auth_token")
        else:
            logger.error(
                f"Unable to authenticate with auth service. Error: {self.authenticator.error_message}"
            )
            raise ConnectionError("Unable to authenticate with auth service.")
        try:
            self.gold_db_conn = get_db_connection(
                ConnectionType.PY_ORACLE, conn_dict=GOLD_CONNECTION
            )
            self.c9k_db_conn = get_db_connection(ConnectionType.SQL, conn_string=CCURE_CONNECTION)
            self.feed_db_conn = get_db_connection(ConnectionType.SQL, conn_string=FEED_CONNECTION)
        except SatDBException as error:
            logger.error(f"{error}")
            raise ConnectionError(f"Unable to connect to database: {error}")
        self.start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        self.end_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        self.gold_query = return_gold_user_query(self.start_date, self.end_date)

    def gold_feed_automation(self) -> dict:
        rows_repaired = self.process_repair()
        # TODO: Restore once PRTG connection is verified.
        # prtg_response = self.notify_prtg_sensor(rows_repaired)
        return rows_repaired

    def process_repair(self) -> dict:
        """
        Look back on gold for all entries in time period
        Check if all the IDs in gold are present in ccure
        Add any missing records back to CCURE
        :return: An integer representing the number of records updated in CCURE
        """
        gold_users = self.fetch_unique_gold_users()
        logger.info(f"got {len(gold_users)} rows from gold")
        if gold_users:
            ccure_users = self.match_ccure_to_gold([x.cidc for x in gold_users])
            logger.info(f"got {len(ccure_users)} matching records from ccure")
            if missed_gold_users := self.find_missed_records(gold_users, ccure_users):
                logger.info(f"found {len(missed_gold_users)} rows to repair")
                return self.add_missing_gold_via_feed(missed_gold_users)
        return {}

    def _gold_results(self):
        cursor = self.gold_db_conn.cursor()
        return cursor.execute(self.gold_query)

    def _ccure_results(self, cid_lst_str):
        ccure_query = return_ccure_user_query(cid_lst_str)
        cursor = self.c9k_db_conn.cursor()
        return cursor.execute(ccure_query)

    def fetch_unique_gold_users(self) -> List[GoldUser]:
        """
        Find all the records in Gold that have been updated within the time period.
        """
        gold_users = []
        for row in self._gold_results():
            gu = GoldUser(row)
            if gu not in gold_users:
                gold_users.append(gu)
        return gold_users

    def match_ccure_to_gold(self, campus_ids: list) -> List[CCureUser]:
        """
        Match records in CCURE with the records in Gold.
        :param campus_ids: a list of campus_ids from GoldUsers to search for in CCURE
        :return: Array of CCureUser that match the campus_ids of GoldUsers
        """
        clist = [campus_ids[x : x + 1000] for x in range(0, len(campus_ids), 1000)]
        ccure_users = []
        for chunk in clist:
            cid_lst_str = "'{}'".format("','".join(chunk))
            for row in self._ccure_results(cid_lst_str):
                cu = CCureUser(row)
                ccure_users.append(cu)
        return ccure_users

    def add_missed_to_ccure(self, missed_gold_users: List[GoldUser]) -> dict:
        """
        TODO: Determine why this does not work. Move towards using the API rather than the feed.
        Write the missing records to the CCURE database
        :param missed_gold_users: List of gold users missing in CCURE
        :return: Number of records successfully updated in CCURE
        """
        update_results = {
            "success": 0,
            "not_in_peoplesoft": 0,
            "failed_ccure_update": 0,
        }
        logger.info("Updating CCURE with missing records")
        for gold_user in missed_gold_users:
            people_soft_response = self.get_peoplesoft_person_request(gold_user.campus_id)
            if people_soft_response.status_code != 200 or len(people_soft_response.json()) == 0:
                failure_message = (
                    f"Failed to get record  with campus_id {gold_user.campus_id} "
                    f"from people soft proxy api due to: {people_soft_response.text},"
                )
                logger.info(failure_message)
                update_results["not_in_peoplesoft"] += 1
            else:
                people_soft_record = people_soft_response.json()[0]
                gold_user.ouc = people_soft_record.get("ouc")
                ccure_response = self.persist_to_ccure_api_request(gold_user)
                if ccure_response.status_code != 200:
                    failure_message = (
                        f"Failed to persist record with campus_id {gold_user.campus_id} "
                        f"using CCURE api. Error: {ccure_response.text}"
                    )
                    logger.info(failure_message)
                    update_results["failed_ccure_update"] += 1
                else:
                    update_results["success"] += 1
        return update_results

    def add_missing_gold_via_feed(self, missed_gold_users: List[GoldUser]) -> dict:
        logger.info("Adding new and updated records to the UserFeed")
        cursor = self.feed_db_conn.cursor()
        cursor = cursor.executemany(
            FEED_INSERT_QUERY, [x.user_feed_vals() for x in missed_gold_users]
        )
        cursor.commit()
        return {
            "supplied": len(missed_gold_users),
            "inserted": cursor.rowcount,
            "campus_ids": [x.campus_id for x in missed_gold_users],
        }

    @staticmethod
    def find_missed_records(
        gold_users: list[GoldUser], ccure_users: list[CCureUser]
    ) -> list[GoldUser]:
        """
        Find missing records in CCURE by comparing the changes in gold with what is in CCURE
        :param gold_users: List of GoldUser objects
        :param ccure_users: List of CCureUser objects
        :return: Records in Gold that are not present in CCURE.
        """
        altered_gold_users = []
        missing_gold_users = []
        for gu in gold_users:
            if gu not in ccure_users:
                missing_gold_users.append(gu)
                continue
            for cu in ccure_users:
                if gu == cu and gu.prox_card_id != cu.prox_card_id:
                    altered_gold_users.append(gu)
        return altered_gold_users + missing_gold_users

    @staticmethod
    def notify_prtg_sensor(value: int) -> None:
        """
        utility function to report success/failure to monitoring system
        :param value: The value to report
        :return: response status code
        """
        response = requests.get(f"{GOLD_PRTG_URL}/?value={value}", timeout=300)
        if response.status_code != 200:
            logger.info("Maintenance report Failed")
        logger.info("Maintenance report Successful")

    def persist_to_ccure_api_request(self, gold_user: GoldUser) -> requests.Response:
        columns, values = gold_user.ccure_cols_and_vals()
        response = requests.post(
            f"{settings.CLEARANCE_SERVICE_URL}/personnel/persist",
            headers={"Authorization": f"Bearer {self.access_token}"},
            json={"property_names": columns, "property_values": values},
            timeout=600,
        )
        return response

    def get_peoplesoft_person_request(self, search: str) -> requests.Response:
        response = requests.get(
            f"{settings.PEOPLESOFT_PROXY_URL}/people?search={search}",
            headers={"Authorization": "Bearer " + self.access_token},
            timeout=600,
        )
        return response


@shared_task
def gold_feed_automation_task():
    logger.info("RUNNING: Gold Feed Automation.")
    gcf = GoldCredentialFeed()
    try:
        results = gcf.gold_feed_automation()
        logger.info("COMPLETE: Gold Feed Automation.")
    except Exception as ex:
        logger.error(f"FAILED: Gold Feed Automation: {ex}")
        slack.send_message(SLACK_CHANNEL, f"FAILED: Gold Feed Automation: {ex}")
        raise ex
    return json.dumps(results)
