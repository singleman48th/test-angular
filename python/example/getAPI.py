import pymysql.cursors  
import connection
from chalice import Chalice
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
from jose import jwt, jwk
from jose.utils import base64url_decode
import requests
import cognito

from flask_cors import CORS
USER_POOL_ID = 'us-east-1_jagQtZSk2'
CLIENT_ID = '11ha6fibtskpt91397thf0meei'
CLIENT_SECRET = '7evc9soe6h8p2dsfkq4as7235sm9em5m9djk96q65tpc1hh141o'
from flask import Flask, request,jsonify
from flask_restful import Resource, Api


global deadpool     # Yes, global. This isn't production code
deadpool = {}
 # Put in your own values. These are fake
deadpool['user_pool_id'] = 'us-east-1_jagQtZSk2'
deadpool['region'] = 'us-east-1'
deadpool['jwks_url'] = 'https://cognito-idp.{}.amazonaws.com/{}/' \
                           '.well-known/jwks.json'.format(
                                   deadpool['region'],
                                   deadpool['user_pool_id'])
deadpool['app_client_id'] = '11ha6fibtskpt91397thf0meei'
deadpool['app_client_secret'] = \
        'https://stackoverflow.com/questions/1306550/' + \
        'calculating-a-sha-hash-with-a-string-secret-key-in-python'
deadpool['username'] = 'minhnv277@gmail.com'
deadpool['password'] = '123456'
deadpool['email'] = 'minhnv277@gmail.com'
deadpool['api_url'] = 'https://' \
        '4a48x6598i.execute-api.eu-central-1.amazonaws.com/prod/insert-login'
app = Flask(__name__)
api = Api(app)
@app.route("/employees") 
def get():
        conn = connection.get_connection()
        sql =  "SELECT * FROM tblTest "
        cursor = conn.cursor()
        cursor.execute(sql)
        payload = []
        content = {}
        for result in cursor:
            content = {'id': result["id"], 'text': result["text"]}
            payload.append(content)
        return jsonify(payload)
@app.route("/employees/<string:id>") 
def getById(id):
        conn = connection.get_connection()
        sql =  "SELECT * FROM tbltest where id = "+ id
        cursor = conn.cursor()
        cursor.execute(sql)
        payload = []
        content = {}
        for result in cursor:
            content = {'id': result["id"], 'name': result["name"]}
            payload.append(content)
        return jsonify(payload)

@app.route('/')
def index():
  cidp = boto3.client('cognito-idp')
  respon = cidp.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': 'minhnv02@ominext.com',
            'PASSWORD': '123456'},
        ClientId=CLIENT_ID)
  token = respon['AuthenticationResult']['AccessToken'] 

  #token = ' eyJraWQiOiJVNDAxTnRVcGFHMFwvTHVCU01YNnU5TFlnZVFPdGRqdlk2RFlSVTZDTmt0RT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI5MTcwODQ1ZS1hODNiLTQ0YjMtYTcwOS01Nzk2OGM4YWIzMzgiLCJldmVudF9pZCI6IjFhZjUwZjBhLTBjOTMtNDg5NC1iOTc5LTdhYTEyYTIxMGUyYiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1OTA0ODU1ODgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2phZ1F0WlNrMiIsImV4cCI6MTU5MDQ4OTE4OCwiaWF0IjoxNTkwNDg1NTg4LCJqdGkiOiJiMjUxOGQ5MS1iMGYxLTRhNjktOTRjYS1hODM5OGZmN2U0YzIiLCJjbGllbnRfaWQiOiIxMWhhNmZpYnRza3B0OTEzOTd0aGYwbWVlaSIsInVzZXJuYW1lIjoiOTE3MDg0NWUtYTgzYi00NGIzLWE3MDktNTc5NjhjOGFiMzM4In0.BXmH5GqOMD4DiMW2zd9-0raKVOb71uGrOJThzYyhhZdueYJJplkp4wpJ8JaWWw_bZ_3WGdUCULpUURg_fGt2_g9523tK0lj25VE8Ysz_koYy6-ci27OOEIG98Sbr4vSjXcf7-BRtT3snpkRHHEgFAglnkBtMBzCwOCtWab-UdlfC6KgBUboripY8ijxG_fOCtYYwpv0YQDeg69qMtpHmmfsTOrHcxz2Rf0YNE_hyZgr1xBna6d115_G5ppiumXd72vvUR8AMyoB_WFYNp7FMHbjy40wPsToSP63UmRnvYeHYm80Z9K-MrQRuz7foYbQYoCZNR04wcNZBvLl0_LSfUA'
  ck = cognito.check_token(token)
  if(ck>0):
   return {'access token': jwt.decode(token,requests.get(deadpool['jwks_url']).json())}
  else:
   return{"authen":"khong thanh cong"}   
@app.route("/create-user")
def createUser():
    client = boto3.client('cognito-idp')
    response = client.admin_create_user(
    UserPoolId=USER_POOL_ID,
    Username='minhnv277@gmail.com',
    UserAttributes=[
        {
            'Name': 'email',
            'Value': 'minhnv277@gmail.com'
        },
    ],
    TemporaryPassword='123456',
    DesiredDeliveryMediums=[
        'EMAIL'
    ]
    )
    return {"result":response}

@app.route("/confirm-signup")
def confirmSignup():
    client = boto3.client('cognito-idp')
    respones = client.confirm_sign_up(
    ClientId=CLIENT_ID,
    Username='minhnv277@gmail.com',
    ConfirmationCode='string'
   )
    return {"result":respones}
 


@app.route('/get-user')
def getUser():
    client = boto3.client('cognito-idp')
    token = 'eyJraWQiOiJVNDAxTnRVcGFHMFwvTHVCU01YNnU5TFlnZVFPdGRqdlk2RFlSVTZDTmt0RT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZjlhNjJmMi05NWJkLTQwM2EtYjEwNS0xMTA3YTIwMzEwN2UiLCJldmVudF9pZCI6Ijc4ODAxYTQ4LWFjNDgtNDQwNy1iYzJjLTZjNDkwNTllYTJiOCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1OTA0OTE2MTEsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2phZ1F0WlNrMiIsImV4cCI6MTU5MDQ5NTIxMSwiaWF0IjoxNTkwNDkxNjExLCJqdGkiOiI5MWFiZmY4Mi1lNjRiLTQ2MDktYjY2Yi03NGQxY2UxOTI3MTEiLCJjbGllbnRfaWQiOiIxMWhhNmZpYnRza3B0OTEzOTd0aGYwbWVlaSIsInVzZXJuYW1lIjoiZWY5YTYyZjItOTViZC00MDNhLWIxMDUtMTEwN2EyMDMxMDdlIn0.KBJU3o7HKXTJozsN0xPfXiH1Z-h7KyDbcaRQ0oSV4pT7PjCDsYbt3pelhyehRi-2qV3HlgnubhgRmvEXq10Eeur3COWXAID7krCQ85CqWpwG780oyATze07VcuK-dPHHRYYc1FT6hxlGaJA6UtDvUn0OhWwHltJzuU8mC-6alTRF9khAEfSR3hBl9wDOlbUFU7ivki5d2yLKt2h4JOTyAOJsoHR9MsBNlVun2F-cWfopxB2HJuC2kzXgIvPr4z8PjA2iv3Y1UlowW09GsXJ-qt0zSQzYnoJWFGorgc_w8dZxCPO85Z9y52kkrAT5ZAQzVOkkACBYnHzuSZzr4iHtCA'
    ck = cognito.check_token(token)
    if(ck>0):
        response =  client.get_user(
                AccessToken=token
                )
        return {"result":response["UserAttributes"]}
    return {"result": "unauthen"}
@app.route('/delete-user')
def deleteUser():
    client = boto3.client('cognito-idp')
    token = 'eyJraWQiOiJVNDAxTnRVcGFHMFwvTHVCU01YNnU5TFlnZVFPdGRqdlk2RFlSVTZDTmt0RT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI5MTcwODQ1ZS1hODNiLTQ0YjMtYTcwOS01Nzk2OGM4YWIzMzgiLCJldmVudF9pZCI6IjFhZjUwZjBhLTBjOTMtNDg5NC1iOTc5LTdhYTEyYTIxMGUyYiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1OTA0ODU1ODgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX2phZ1F0WlNrMiIsImV4cCI6MTU5MDQ4OTE4OCwiaWF0IjoxNTkwNDg1NTg4LCJqdGkiOiJiMjUxOGQ5MS1iMGYxLTRhNjktOTRjYS1hODM5OGZmN2U0YzIiLCJjbGllbnRfaWQiOiIxMWhhNmZpYnRza3B0OTEzOTd0aGYwbWVlaSIsInVzZXJuYW1lIjoiOTE3MDg0NWUtYTgzYi00NGIzLWE3MDktNTc5NjhjOGFiMzM4In0.BXmH5GqOMD4DiMW2zd9-0raKVOb71uGrOJThzYyhhZdueYJJplkp4wpJ8JaWWw_bZ_3WGdUCULpUURg_fGt2_g9523tK0lj25VE8Ysz_koYy6-ci27OOEIG98Sbr4vSjXcf7-BRtT3snpkRHHEgFAglnkBtMBzCwOCtWab-UdlfC6KgBUboripY8ijxG_fOCtYYwpv0YQDeg69qMtpHmmfsTOrHcxz2Rf0YNE_hyZgr1xBna6d115_G5ppiumXd72vvUR8AMyoB_WFYNp7FMHbjy40wPsToSP63UmRnvYeHYm80Z9K-MrQRuz7foYbQYoCZNR04wcNZBvLl0_LSfUA'
    
    ck = cognito.check_token(token)
    if(ck>0):
        response =  client.delete_user(
                AccessToken=token
                )
        return {"result":response}
    return {"result": "unauthen"}

@app.route("/forgot-password")
def forgotPassWord():
    client = boto3.client('cognito-idp')
    response = client.forgot_password(
    ClientId=CLIENT_ID,
    Username='minhnv277@gmail.com'
    )
    return {"result":response}
@app.route("/confirm-forgot-password")
def confirmForgotPassWord():
    client = boto3.client('cognito-idp')
    response = client.confirm_forgot_password(
    ClientId=CLIENT_ID,
    ConfirmationCode ="",
    Username='minhnv277@gmail.com'
    )
    return {"result":response}

@app.route("/employees",methods = ['POST'])
def insertEmployees():
    try:
        text = request.form.get("txt")
        conn =connection.get_connection()
        cs = conn.cursor()
        cu =   cs.callproc('procedure_test', [text,])
        conn.commit()
    except Exception as e:
        print("Failed to execute stored procedure: {}".format(e))
    finally:
        cs.close()
        print("MySQL connection is closed")
    return {"result":cu}




    
if __name__ == '__main__':
    app.run(debug=True)


