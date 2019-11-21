from flask import Flask 
from flask import jsonify
from flask_cors import CORS
import psycopg2
import os
import databaseTables as dt 
import databaseInteractors as di 

PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return ''


@app.route('/user/email/<address>',methods=['GET'])
def checkEmail(address):
    emailExists = di.doesEmailExist(address)
    payload = {'email':address,'exists': emailExists}
    return jsonify(payload)

@app.route('/general/init',methods=['POST'])
def init():
    dt.dropTable('user')
    dt.initialiseUserTable()
    dt.addUserDummy()
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
