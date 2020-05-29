from chalice import Chalice
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
USER_POOL_ID = 'us-east-1_YdrJuugg4'
CLIENT_ID = '6vsdg62umcpmkm47rfu5ro5gsj'
CLIENT_SECRET = '7evc9soe6h8p2dsfkq4as7235sm9em5m9djk96q65tpc1hh141o'

app = Chalice(app_name='helloworld')
def get_secret_hash(username):
  msg = username + CLIENT_ID 
  dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
  msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
  d2 = base64.b64encode(dig).decode()
  return d2
def initiate_auth(client, username, password):
  secret_hash = get_secret_hash(username)
  try:
    resp = client.admin_initiate_auth(
                 UserPoolId=USER_POOL_ID,
                 ClientId=CLIENT_ID,
                 AuthFlow='ADMIN_NO_SRP_AUTH',
                 AuthParameters={
                     'USERNAME': username,
                     'SECRET_HASH': secret_hash,
                     'PASSWORD': password,
                  },
                ClientMetadata={
                  'username': username,
                  'password': password,
              })
  except client.exceptions.NotAuthorizedException:
    return None, "The username or password is incorrect"
  except client.exceptions.UserNotConfirmedException:
        return None, "User is not confirmed"
  except Exception as e:
        return None, e.__str__()
  return resp, None
def lambda_handler(event, context):
   client = boto3.client('cognito-idp')
   for field in ["username", "password"]:
     if event.get(field) is None:
       return  {"error": True, 
                "success": False, 
                "message": f"{field} is required", 
                "data": None}
   resp, msg = initiate_auth(client, "minhnv277@gmail.com", "123456")
   if msg != None:
      return {'message': msg, 
              "error": True, "success": False, "data": None}
   if resp.get("AuthenticationResult"):
      return {'message': "success", 
               "error": False, 
               "success": True, 
               "data": {
               "id_token": resp["AuthenticationResult"]["IdToken"],
      "refresh_token": resp["AuthenticationResult"]["RefreshToken"],
      "access_token": resp["AuthenticationResult"]["AccessToken"],
      "expires_in": resp["AuthenticationResult"]["ExpiresIn"],
      "token_type": resp["AuthenticationResult"]["TokenType"],
                    }
              }
   else: #this code block is relevant only when MFA is enabled
        return {"error": True, 
           "success": False, 
           "data": None, "message": None}







@app.route('/')
def index():
    client = boto3.client('cognito-idp')
    resp = client.admin_initiate_auth(
        UserPoolId=USER_POOL_ID,
        ClientId=CLIENT_ID,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": "minhnv277@gmail.com",
            "PASSWORD": "123456"
        }
    )

    return {'hello': resp['AuthenticationResult']['AccessToken']}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
