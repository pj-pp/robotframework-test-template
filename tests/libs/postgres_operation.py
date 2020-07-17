import psycopg2
import pprint
import uuid
from datetime import datetime


def get_datetime_now():
    get_date_str = datetime.utcnow().isoformat(sep=' ', timespec='microseconds')
    return get_date_str


def get_connection_string(db_host, database_name, username, password):

    conn_string = "host='%s' dbname='%s' user='%s' password='%s' port='5432'" % (
        db_host, database_name, username, password)
    print("Connecting to database\n	->%s" % (conn_string))
    return conn_string


def verify_email_user(conn_string, verified_email):

    datetime_str = get_datetime_now()

    sql = '''
        UPDATE users
        SET verified_email_at = '{datetime_str}'
        WHERE email = '{email}'
        '''.format(datetime_str=datetime_str, email=verified_email)
    print("SQL : " + sql)
    try:
        print("Connecting to database\n	->%s" % (conn_string))
        # connect to the PostgreSQL database
        conn = psycopg2.connect(conn_string)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (verified_email))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def query_user_uid(conn_string, verified_email):

    sql = '''
        SELECT uid
        FROM users
        WHERE email = '{email}'
        '''.format(email=verified_email)

    print("SQL : " + sql)
    try:
        print("Connecting to database\n	->%s" % (conn_string))
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        cur.execute(sql, (verified_email))
        user_uid = str(cur.fetchone()[0])
        print(user_uid)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_uid


def user_infos_insert(conn_string, user_uid, scan_id, datetime_str):

    if user_uid.startswith("user_"):
        user_infos = "user_info_"+user_uid[10:]
        print(user_infos)

    sql = '''
        INSERT INTO "public"."user_infos" ("uid", "user_uid", "first_name", "last_name", "middle_name", "dob", "address", "city", "state", "country", "inserted_at", "updated_at")
        VALUES ('{user_infos}',
            '{user_uid}',
            '{scanid}',
            'ohmyqa',
            NULL,
            '1981-06-12',
            'ohmyqa',
            'ohmyqa',
            'ohmyqa',
            'THA',
            '{datetime_str}',
            '{datetime_str}')
        '''.format(user_infos=user_infos,user_uid=user_uid, scanid=scan_id, datetime_str=datetime_str)

    print("SQL : " + sql)
    try:
        print("Connecting to database\n	->%s" % (conn_string))
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def kycs_user_insert(conn_string, user_uid, scan_id, datetime_str):

    if user_uid.startswith("user_"):
        kyc_user = "kyc_"+user_uid[5:]
        print(kyc_user)

    # Dummy string
    redirect_url = 'https://test-omise.netverify.com/web/v4/app?authorizationToken=eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAB3MvQ6CMBAA4He5mSbt9fqDmz9giJGBEBK7mB4HiwuDg8T47qL7l-8N02v_hJ1xPjokQ7GMVEBuBHZgvTbIsygbpqjIlFnlObCSkYwnH7IVhALGbpo3_VjHuzanOrkDYTyjTm1q3dCblI7Xy8_9U9SMxsmkSvasKGhUUYJVLC6zDVFYaMNLvy6bbqt-qLqmvsHnC7pKCOerAAAA.LJD3vnNUpacVnYn70CkHiPWjenrq28Xnssc5sWj6jytD8I_z8xILd3KRp3cHSSKAY1C_jyGdRk3SX8IskGZHpg&locale=en'
    tx_info = '{"date": "2019-07-17T05:09:09.012000", "source": "WEB_UPLOAD", "status": "DONE", "client_ip": "58.181.243.195"}'
    doc_info = '{"dob": "1981-06-14", "type": "ID_CARD", "expiry": "2025-06-13", "number": "3 2009 00214 13 1", "status": "APPROVED_VERIFIED", "address": null, "us_state": null, "last_name": "Wilarat", "first_name": "Nattapol", "id_sub_type": null, "issuing_date": null, "issuing_place": null, "issuing_country": "THA", "personal_number": null, "issuing_authority": null}'
    verification_info = '{"mrz_check": "NOT_AVAILABLE", "reject_reason": null, "identity_verification": {"reason": null, "validity": "true", "similarity": "MATCH", "handwritten_note_matches": null}}'

    sql = '''
        INSERT INTO "public"."kycs" ("uid", "status", "user_uid", "scan_reference", "created_at", "redirect_url", "tx_info", "doc_info", "verification_info", "inserted_at", "updated_at")
        VALUES ('{kycid}',
            'completed',
            '{uid}',
            '{scanid}',
            '{datetime_str}',
            '{redirect_url}',
            '{tx_info}',
            '{doc_info}',
            '{verification_info}',
            '{datetime_str}',
            '{datetime_str}')
        '''.format(kycid=kyc_user,uid=user_uid, scanid=scan_id, datetime_str=datetime_str,
                   redirect_url=redirect_url, tx_info=tx_info, doc_info=doc_info, verification_info=verification_info)

    print("SQL : " + sql)
    try:
        print("Connecting to database\n	->%s" % (conn_string))
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def kycs_user_process(conn_string, verified_email):
    # Get uid by email
    user_uid = query_user_uid(conn_string, verified_email)
    print("uid = %s" % (user_uid))

    scan_id = uuid.uuid4()  # random uuid number
    datetime_str = get_datetime_now()  # get the current date time in ISO format

    kycs_user_insert(conn_string, user_uid, scan_id, datetime_str)  # Insert user into kycs table
    # user_infos_insert(conn_string, user_uid, scan_id, datetime_str)  # Insert user into kycs table

    return 0
