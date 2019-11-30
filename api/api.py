from flask import Flask , jsonify, request, _request_ctx_stack
from flask_cors import CORS, cross_origin
import psycopg2
import os
import json
from six.moves.urllib.request import urlopen
from functools import wraps
from jose import jwt

import databaseTables as dt 
import databaseInteractors as di 

PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']
AUTH0_DOMAIN = os.environ['AUTH0DOMAIN']
API_AUDIENCE =  os.environ['AUTH0AUDIENCE']
ALGORITHMS = ["RS256"]


app = Flask(__name__)
CORS(app)

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

def get_token_auth_header():
    auth = request.headers.get("Authorization",None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)
    
    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code":"invalid_header",
                         "description":
                         "Authorization header must start with"
                         " Bearer"}, 401)
    
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)
    
    token = parts[1]

    return token

def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated


@app.route('/')
def home():
    return ''


@app.route('/user/email/<email>',methods=['GET'])
@cross_origin(headers=["Content-Type","Authorization"])
@requires_auth 
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

@app.route('/user/<email>',methods=['PUT'])
def updateUser(email):
    data = json.loads(request.data.decode())
    username = data['username']
    email = data['email']
    firstname = data['firstname']
    lastname = data['lastname']
    gender = data['gender']
    age = data['age']

    sucess, reason = di.updateUser(username,email,firstname,lastname,gender,age)
    payload = {'sucess':sucess, 'reason':reason}
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
