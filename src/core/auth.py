import jwt
import datetime
from dynaconf import settings
from flask import abort

jwt_alg = settings['JWT_ALG']
jwt_expire = settings['JWT_EXPIRE']
jwt_secret_key = settings['JWT_SECRET_KEY']


def make_jwt(data: dict):
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=jwt_expire),
        'iat': datetime.datetime.now(),
    }
    payload.update(data)

    headers = {
        'alg': jwt_alg,
    }

    token = jwt.encode(payload, jwt_secret_key, algorithm=jwt_alg, headers=headers)
    return {'token': token, 'expires_time': int(datetime.datetime.timestamp(payload['exp']))}


def check_jwt(token: str):
    try:
        data = jwt.decode(token, jwt_secret_key, algorithms=[jwt_alg])
        return data
    except Exception as e:
        abort(401, e)
