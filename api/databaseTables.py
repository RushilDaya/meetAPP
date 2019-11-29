# the database schema is defined in this file
# as a series of functions which can be called to initialise tables as well as DROP all the tables
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

def dropTable(tableName):
    conn, cursor = getConnectionAndCursor()
    drop_table ='''DROP TABLE IF EXISTS users ;'''

    cursor.execute(drop_table)
    conn.commit()
    cursor.close()
    conn.close()
    
    return True

def initialiseUserTable():
    conn, cursor = getConnectionAndCursor()
    create_user_table_if_ne = '''
        CREATE TABLE IF NOT EXISTS users (
            username varchar(255) UNIQUE NOT NULL,
            email varchar(255) PRIMARY KEY NOT NULL,
            firstname varchar(255) NOT NULL, 
            lastname varchar(255) NOT NULL,
            age integer NOT NULL,
            gender varchar(1) NOT NULL
        );
    '''
    cursor.execute(create_user_table_if_ne)
    conn.commit()
    cursor.close()
    conn.close()
    return True

def addUserDummy():
    conn, cursor = getConnectionAndCursor()
    insert_dummy_record = '''
        INSERT INTO users (username, email, firstname, lastname,
        age,gender) VALUES ('jondoe', 'jondoe@abc.com', 'jon',
        'doe',21,'M');
    '''
    cursor.execute(insert_dummy_record)
    conn.commit()
    cursor.close()
    conn.close()
    return True

    