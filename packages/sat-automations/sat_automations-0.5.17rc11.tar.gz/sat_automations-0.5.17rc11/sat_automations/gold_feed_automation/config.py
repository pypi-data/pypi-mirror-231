from django.conf import settings

GOLD_PRTG_URL = f"{settings.GOLD_PRTG_BASE_URL}/{settings.GOLD_PRTG_GUID}"

GOLD_CONNECTION = {
    "user": settings.GOLD_DB_USERNAME,
    "password": settings.GOLD_DB_PASSWORD,
    "dsn": settings.GOLD_DB_DSN,
}

CCURE_CONNECTION = (
    "DRIVER=FreeTDS;"
    f"SERVER={settings.CCURE_SERVER};"
    f"PORT={settings.CCURE_PORT};"
    f"UID={settings.CCURE_USERNAME};"
    f"PWD={settings.CCURE_PASSWORD};"
)

FEED_CONNECTION = (
    "DRIVER=FreeTDS;"
    f"SERVER={settings.FEED_SERVER};"
    f"PORT={settings.FEED_PORT};"
    f"UID={settings.FEED_USERNAME};"
    f"PWD={settings.FEED_PASSWORD};"
)

FEED_INSERT_QUERY = """
        INSERT INTO DataFeed.dbo.UserFeed(
        [PatronID]
        ,[CampusID]
        ,[FirstName]
        ,[MiddleName]
        ,[LastName]
        ,[Classification]
        ,[Email]
        ,[Type]
        ,[Department]
        ,[PersonnelType]
        ,[ProxCardID]
        ,[CIDC]
        ,[GoldTimeStamp]
        )
        VALUES (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
        )
        """
