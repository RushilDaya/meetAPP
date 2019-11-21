# functions which interact with the database tables, assumes that tables are initialised

import psycopg2
import os

PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']


def getConnectionAndCursor():
    conn = psycopg2.connect(user=PGUSER, password=PGPASSWORD,host=PGHOST,
                            port=PGPORT,database=PGDATABASE)
    cursor = conn.cursor()
    return conn,cursor 

def doesEmailExist(email):
    conn, cursor = getConnectionAndCursor()

    email_records = '''
        SELECT * FROM users WHERE email='%s' ;
    ''' % email 
    cursor.execute(email_records)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if len(rows) == 0:
        return False
    if len(rows) == 1:
        return True
    raise Exception('corrupt db')
