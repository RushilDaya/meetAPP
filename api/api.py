from flask import Flask 
from flask_cors import CORS
import psycopg2
import os

PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    conn = psycopg2.connect(user=PGUSER, password=PGPASSWORD,host=PGHOST,
                            port=PGPORT,database=PGDATABASE)
    cursor = conn.cursor()
    create_table_if_ne = '''
        CREATE TABLE IF NOT EXISTS cretin (
            id integer PRIMARY KEY NOT NULL,
            count integer NOT NULL 
        );
    '''
    cursor.execute(create_table_if_ne)
    conn.commit()

    init_counter  = '''
    INSERT INTO cretin (id,count) VALUES ('1', '0') ON CONFLICT (id) DO NOTHING;
    '''
    cursor.execute(init_counter)
    conn.commit()

    get_count = '''
    SELECT count FROM cretin WHERE id='1';
    '''
    cursor.execute(get_count)
    records = cursor.fetchall()


    count = records[0][0]
    print(count)

    count+=1

    update_count = '''
    UPDATE cretin SET count = %s WHERE id='1';
    '''
    cursor.execute(update_count,(str(count),))
    conn.commit()

    cursor.close()
    conn.close()

    print(count)
    return str(count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
