import pytest

from sat_automations.gold_feed_automation.tasks import GoldCredentialFeed
from sat_automations.gold_feed_automation.tests.fixtures import FAKE_CCURE_DATA, FAKE_GOLD_DATA


@pytest.fixture
def gold_feed_mocks(mocker):
    ga = mocker.patch("sat_automations.gold_feed_automation.tasks.GoogleAuthenticate")
    db_conns = mocker.patch("sat_automations.gold_feed_automation.tasks.get_db_connection")
    gold_query = mocker.patch("sat_automations.gold_feed_automation.tasks.return_gold_user_query")
    gcf = mocker.patch(
        "sat_automations.gold_feed_automation.tasks.GoldCredentialFeed._gold_results",
        return_value=[list(x.values()) for x in FAKE_GOLD_DATA],
    )
    yield ga, db_conns, gold_query, gcf


def test_gold_feed_reduction(gold_feed_mocks):
    """
    The fetch_gold_users method's purpose is to get a list of
    gold users within a timeframe and then remove any duplicates
    based on the patron_id and cidc.

    This test ensures that the method is removing duplicates that
    are older than the most recent record.
    :param gold_feed_mocks:
    :return:
    """
    gold_feed = GoldCredentialFeed()
    reduced = gold_feed.fetch_unique_gold_users()
    # The reduction should have removed 7 records
    assert len(FAKE_GOLD_DATA) - len(reduced) == 7
    assert reduced[0].campus_id == "200408152"
    assert reduced[0].datetime_as_string == "2023-08-30 13:17:16"
    # The duplicate of this record is gone.
    assert len([x for x in reduced if x.campus_id == "200408152"]) == 1


def test_missing_gold_users(mocker, gold_feed_mocks):
    mocker.patch(
        "sat_automations.gold_feed_automation.tasks.GoldCredentialFeed._ccure_results",
        return_value=[list(x.values()) for x in FAKE_CCURE_DATA],
    )
    gold_feed = GoldCredentialFeed()
    reduced = gold_feed.fetch_unique_gold_users()
    ccure_matches = gold_feed.match_ccure_to_gold([x.cidc for x in reduced])
    unmatched_gold_users = gold_feed.find_missed_records(reduced, ccure_matches)
    # 10 records, 8 are not in ccure and 1 has a different prox_card_id in ccure.
    # The GoldFeed is considered to be the source of truth, so the gold record is
    # considered to be the correct one.
    assert len(unmatched_gold_users) == 9
