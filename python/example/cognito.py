import argparse
import boto3
import requests
from botocore.exceptions import ClientError
from pprint import pprint
from jose import jwt, jwk
from jose.utils import base64url_decode

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

def sign_up():
    cidp = boto3.client('cognito-idp')

    try:
        # Add user to pool
        sign_up_response = cidp.sign_up(
                ClientId=deadpool['app_client_id'],
                Username=deadpool['username'],
                Password=deadpool['password'],
                UserAttributes=[{'Name': 'email',
                                 'Value': deadpool['email']}])
        pprint(sign_up_response)
        print("    Confirming user...")
        # Use Admin powers to confirm user. Normally the user would
        # have to provide a code or click a link received by email
        confirm_sign_up_response = cidp.admin_confirm_sign_up(
                UserPoolId=deadpool['user_pool_id'],
                Username=deadpool['username'])
        pprint(confirm_sign_up_response)
    except ClientError as err:
        # Probably user already exists
        print(err)


def init_auth():
    # Log in the user we just created
    global deadpool
    cidp = boto3.client('cognito-idp')

    # This is less secure, but simpler
    response = cidp.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': deadpool['username'],
                'PASSWORD': deadpool['password']},
            ClientId=deadpool['app_client_id'])
    print("----- Log in response -----")
    pprint(response)
    print("---------------------------")
    # AWS official docs on using tokens with user pools:
    # https://amzn.to/2HbmJG6
    # If authentication was successful we got three tokens
    deadpool['jwt_access_token'] = \
        response['AuthenticationResult']['AccessToken']
    deadpool['jwt_id_token'] = \
        response['AuthenticationResult']['IdToken']
    deadpool['jwt_refresh_token'] = \
        response['AuthenticationResult']['RefreshToken']


def check_token(token):
    bcheck = 0
    # AWS docs on verifying tokens:
    # https://amzn.to/2vUwFx7
    # Decode token header
    try:
     token_header = jwt.get_unverified_header(token)
    except:
        return 0
    print('Token header:')
    pprint(token_header)
    # Decode token payload
    token_claims = jwt.get_unverified_claims(token)
    print('Token claims:')
    pprint(token_claims)
    # Verify signature, step by step.
    # Original (and better) code in this gist: https://bit.ly/2E3fAFP
    print('Checking key manually')
    # First, get the JSON Web Key Set, which contains two public
    # keys corresponding to the two private keys that could
    # have been used to sign the token.
    r = requests.get(deadpool['jwks_url'])
    if r.status_code == 200:
        jwks = r.json()
    else:
        raise 'Did not retrieve JWKS, got {}'.format(r.status_code)
    # The token header contains a field named 'kid', which stands
    # for Key ID. The JWKS also contains two 'kid' fields, one for
    # each key. The 'kid' in the header tells us which public key
    # must be used to verify the signature.
    kid = token_header['kid']
    # Search the JWKS for the proper public key
    key_index = -1
    for i in range(len(jwks['keys'])):
        if kid == jwks['keys'][i]['kid']:
            key_index = i
            break
    if key_index == -1:
        print('Public key not found, can not verify token')
    else:
        # Convert public key
        public_key = jwk.construct(jwks['keys'][key_index])
        # Get claims and signature from token
        claims, encoded_signature = token.rsplit('.', 1)
        # Verify signature
        decoded_signature = base64url_decode(
                encoded_signature.encode('utf-8'))
        if not public_key.verify(claims.encode("utf8"),
                                 decoded_signature):
            print('Signature verification failed')
        else:
            bcheck = 1
            print('Signature successfully verified')
    if bcheck > 0:
        return 1
    else:
        return 0




def decode_token(token):
    # Executing decode() on the token will return the header or raise
    # an error if checking the signature or one of the claims fails.
    # See https://python-jose.readthedocs.io/en/latest/jwt/api.html
    pprint(jwt.decode(
        token,
        requests.get(deadpool['jwks_url']).json()))


def call_api(token):
    headers = {'Authorization': token}
    url = deadpool['api_url']
    r = requests.post(url, headers=headers)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    optparser = argparse.ArgumentParser(description='Cognito demo')
    optparser.add_argument('-p',
                           '--profile',
                           help='aws credentials profile')
    args = optparser.parse_args()

    if args.profile:
        boto3.setup_default_session(profile_name=args.profile)


   

    print('Signing up...')
    #sign_up()
    print('Authenticating...')
    #init_auth()
    print('"Manually" check access token...')
    #check_token(deadpool['jwt_id_token'])
    print('Decode token, also runs checks...')
    #decode_token(deadpool['jwt_access_token'])
    print('POST to API...')
    #call_api(deadpool['jwt_id_token'])