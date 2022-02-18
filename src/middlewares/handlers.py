from flask import request, abort, g
from src.common.app import app
from src.core.auth import check_jwt
from src.common.http.response import JsonResponse
from src.common.http.rc import RC
from src.common.api import api
from dynaconf import settings


@app.before_request
def process_check_authentication():
    """
    
    """
    if request.method != 'OPTIONS':
        with open(settings['white_list'], 'r') as f:
            white_list = [l.strip() for l in f.readlines()]
        for free_url in white_list:
            if request.path.startswith(free_url):
                return

        token = request.headers.get('Authorization')
        user = check_jwt(token)
        if not user:
            abort(401, '未授权')
        g.user = user


@app.before_request
def process_check_permission():
    """
    校验权限
    """
    # print('-----> 校验权限', g.user)


@api.app.errorhandler(401)
def error_401(error):
    return JsonResponse(rc=RC.no_auth.value, error="权限错误", message=str(error.description))

@api.app.errorhandler(400)
def error_400(error):
    return JsonResponse(rc=RC.invalid.value, error="请求失败", message=str(error.description))


# @app.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin']='*'
#     environ.headers['Access-Control-Allow-Method']='*'
#     environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
#     return environ
