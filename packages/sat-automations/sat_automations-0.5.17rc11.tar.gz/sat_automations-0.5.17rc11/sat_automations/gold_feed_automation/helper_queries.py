
def return_ccure_user_query(campus_id_str_list):
    ccureUserQuery = f"""
                    SELECT
                        cre.CardInt1 AS "PatronID",
                        p.text1 AS "CampusID",
                        p.FirstName AS "FirstName",
                        p.LastName AS "LastName",
                        p.MiddleName AS "MiddleName",
                        p.text16 AS "Classification",
                        p.text14 AS "Email",
                        pudf.Department_ AS "Department",
                        pt.Name AS "PersonnelType",
                        cre.CardNumber AS "ProxCardID",
                        p.text12 AS "CIDC"
                    FROM
                        ACVSCore.Access.Personnel AS p
                        INNER JOIN ACVSCore.Access.PersonnelType AS pt WITH ( nolock ) ON p.PersonnelTypeID = pt.ObjectID
                        LEFT JOIN acvscore.access.PersonnelUDF AS pudf WITH ( nolock ) ON p.ObjectID = pudf.ObjectID
                        INNER JOIN ACVSCore.Access.Credential AS cre WITH ( nolock ) ON p.ObjectID = cre.PersonnelId
                    WHERE
                        p.text12 in ({campus_id_str_list})
                    """
    return ccureUserQuery


def return_gold_user_query(start_date, end_date):
    return f"""
                -- Working Key History Map
                SELECT
                p.ID_PERS AS "PatronID",
                p.VAL_UNIV_ID AS "CampusID",
                p.VAL_NAM_FIRST AS "FirstName",
                p.VAL_NAM_MIDDLE AS "MiddleName",
                p.VAL_NAM_LAST AS "LastName",
                p.CLASSIFICATION AS "Classification",
                i.DBD_EMAIL AS "Email",
                'EDIT' AS "Type",
                i.LOCAL_DEPARTMENT AS "Department",
                cl.CARDSTOCKTYPE AS "PersonnelType",
                kmh.KEYVALUE AS "ProxCardID",
                p.VAL_UNIV_ID||':0' AS "CIDC",
                kmh.MODIFICATIONDATE AS "UpdateTimeStamp"
                FROM DIEBOLD.PERS p
                LEFT JOIN DIEBOLD.EXTENDEDPATRONINFO i
                    ON p.ID_PERS = i.PATRONID
                LEFT JOIN DIEBOLD.PATRONIMAGES im
                    ON p.ID_PERS = im.PATRONID
                LEFT JOIN DIEBOLD.PATRONCARDLOG cl
                    ON p.ID_PERS = cl.PATRONID
                    AND    POSTDATE > (SELECT (MAX(POSTDATE) -1) FROM PATRONCARDLOG
                                       WHERE POSTDATE <= TO_DATE('{end_date}', 'yyyy-mm-dd hh24:mi:ss'))
                JOIN DIEBOLD.KEYMAPPINGINFO_HISTORY kmh
                    ON p.ID_PERS = kmh.PATRONID
                    AND kmh.MEDIATYPE = 22
                    AND kmh.MODIFICATIONTYPE = 'UPDATE'
                    AND kmh.MODIFICATIONDATE > TO_DATE('{start_date}', 'yyyy-mm-dd hh24:mi:ss')
                    AND kmh.MODIFICATIONDATE <= TO_DATE('{end_date}', 'yyyy-mm-dd hh24:mi:ss')
                UNION
                -- Working CardLog
                SELECT
                p.ID_PERS AS "PatronID",
                p.VAL_UNIV_ID AS "CampusID",
                p.VAL_NAM_FIRST AS "FirstName",
                p.VAL_NAM_MIDDLE AS "MiddleName",
                p.VAL_NAM_LAST AS "LastName",
                p.CLASSIFICATION AS "Classification",
                i.DBD_EMAIL AS "Email",
                'CARD' AS "Type",
                i.LOCAL_DEPARTMENT AS "Department",
                cl.CARDSTOCKTYPE AS "PersonnelType",
                k.KEYVALUE AS "ProxCardID",
                p.VAL_UNIV_ID||':0' AS "CIDC",
                cl.POSTDATE AS "UpdateTimeStamp"
                FROM DIEBOLD.PERS p
                LEFT JOIN DIEBOLD.EXTENDEDPATRONINFO i
                   ON p.ID_PERS = i.PATRONID
                LEFT JOIN DIEBOLD.PATRONIMAGES im
                    ON p.ID_PERS = im.PATRONID
                JOIN DIEBOLD.PATRONCARDLOG cl
                    ON p.ID_PERS = cl.PATRONID
                JOIN DIEBOLD.KEYMAPPINGINFO k
                    ON p.ID_PERS = k.PATRONID
                    AND k.MEDIATYPE = 22
                WHERE
                    cl.POSTDATE > TO_DATE('{start_date}', 'yyyy-mm-dd hh24:mi:ss')
                    AND cl.POSTDATE = (
                        SELECT
                            MAX( POSTDATE )
                        FROM
                            PATRONCARDLOG
                        WHERE
                            PATRONID = p.ID_PERS
                            AND cl.POSTDATE <= TO_DATE('{end_date}', 'yyyy-mm-dd hh24:mi:ss')
                        )
                -- Most Recent Card Activity Filter
                ORDER BY 13 DESC
                """
