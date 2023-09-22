CCURE_COLUMN_HEADERS = [
    "CardInt1",
    "Text1",
    "FirstName",
    "MiddleName",
    "LastName",
    "Text16",
    "Text14",
    "Department",
    "PersonnelType",
    "CardNumber",
    "Text12",
    "Int1",
]

USER_FEED_COLUMN_HEADERS = [
    "PatronID",
    "CampusID",
    "FirstName",
    "MiddleName",
    "LastName",
    "Classification",
    "Email",
    "Type",
    "Department",
    "PersonnelType",
    "ProxCardID",
    "CIDC",
    "GoldTimeStamp",
]


class UserBase:
    """
    TODO: currently these campus ids have a :0 appended to them. There
    was a historical reason for this, but it may not be necessary anymore.
    """

    def __init__(self, row) -> None:
        self.patron_id = row[0]
        self.campus_id = row[1]
        self.first_name = row[2]
        # 3 and 4 are in different order for gold and ccure
        self.classification = row[5] if row[5] else ""
        self.email = row[6]
        # row[7] is 'type' in gold and 'department' in ccure
        self.__prox_card_id = None
        self.cidc = None
        self.update_timestamp = None
        self.ouc = ""

    def __str__(self):
        return f"{self.email} (CIDC: {self.cidc} ProxID: {self.prox_card_id})"

    def __eq__(self, other):
        return (self.patron_id, self.cidc) == (other.patron_id, other.cidc)

    @property
    def datetime_as_string(self):
        return self.update_timestamp.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def feed_classification(self):
        return self.classification.upper()[:5]


class GoldUser(UserBase):
    def __init__(self, row) -> None:
        super().__init__(row)
        self.middle_name = row[3]
        self.last_name = row[4]
        # row[5] is classification
        # row[6] is email
        self.type = row[7]
        self.department = row[8]
        self.personnel_type = row[9]
        self.__prox_card_id = row[10]
        self.cidc = row[11]
        self.update_timestamp = row[12]

    def ccure_cols_and_vals(self):
        property_values = [
            self.patron_id,
            self.campus_id,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.classification,
            self.email,
            self.department,
            self.personnel_type,
            self.prox_card_id,
            self.cidc,
            self.ouc,
        ]
        return CCURE_COLUMN_HEADERS, property_values

    def user_feed_vals(self) -> list:
        """
        Return the values for the user feed table
        :return:
        """
        return [
            self.patron_id,
            self.campus_id,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.classification,
            self.email,
            self.type,
            self.department,
            self.personnel_type,
            self.prox_card_id,
            self.cidc,
            self.datetime_as_string,
        ]

    @property
    def prox_card_id(self):
        return str(self.__prox_card_id).zfill(7)


class CCureUser(UserBase):
    def __init__(self, row):
        super().__init__(row)
        self.last_name = row[3]
        self.middle_name = row[4]
        # row[5] is classification
        # row[6] is email
        self.department = row[7]
        self.personnel_type = row[8]
        self.__prox_card_id = row[9]
        self.cidc = row[10]

    @property
    def prox_card_id(self):
        return str(self.__prox_card_id).zfill(7)
