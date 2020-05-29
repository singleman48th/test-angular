import json
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import uuid
USER_POOL_ID = ' us-east-1_MojhY5aRD'
CLIENT_ID = '5ipq8qq7ftibge3sc6679lbu86'
CLIENT_SECRET ='12r14o3i2m78pbt12j6plrgjm77e4pf4ch9s618rvn447eiu4rvi'
def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'),   digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2
def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    try:
        username = event['username']
        password = event['password']
        code = event['code']
        client.confirm_forgot_password(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            ConfirmationCode=code,
            Password=password,
           )
    except client.exceptions.UserNotFoundException as e:
        return {"error": True, 
                "success": False,
                "data":  None,
                "message": "Username doesnt exists"}
        
    except client.exceptions.CodeMismatchException as e:
        return {"error": True, 
               "success": False,
               "data": None,
               "message": "Invalid Verification code"}
        
    except client.exceptions.NotAuthorizedException as e:
        return {"error": True, 
                 "success": False, 
                 "data": None, 
                 "message": "User is already confirmed"}
    
    except Exception as e:
        return {"error": True, 
                "success": False,
                "data": None,
                "message": f"Unknown error {e.__str__()} "}
      
    return {"error": False, 
            "success": True, 
            "message": f"Password has been changed successfully",
            "data": None}