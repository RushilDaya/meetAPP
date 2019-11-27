from flask import Flask 
from flask import jsonify
from flask import request
from flask_cors import CORS
import psycopg2
import os
import databaseTables as dt 
import databaseInteractors as di 
import json

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


@app.route('/user/email/<email>',methods=['GET'])
def checkEmail(email):
    emailExists = di.doesEmailExist(email)
    payload = {'email':email,'exists': emailExists}
    return jsonify(payload)

@app.route('/user/create',methods=['POST'])
def createNewUser():
    data = json.loads(request.data.decode())
    username = data['username']
    email = data['email']
    firstname = data['firstname']
    lastname = data['lastname']
    gender = data['gender']
    age = data['age']

    success,reason = di.tryCreateNewUser(username,email,firstname,lastname,gender,age)
    payload = {'success':success,'reason':reason}
    
    return jsonify(payload)

@app.route('/user/<email>',methods=['GET'])
def getUser(email):
    emailExists = di.doesEmailExist(email)
    if not emailExists:
        payload = {'sucess':False,'reason':'user not found'}
    if emailExists:
        payload = di.getUserData(email)
    return jsonify(payload)

        

@app.route('/general/init',methods=['POST'])
def init():
    dt.dropTable('user')
    dt.initialiseUserTable()
    dt.addUserDummy()
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
