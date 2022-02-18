from flask import request, abort, views, g
from src.common.http.response import JsonResponse
from src.conf.settings import settings
from src.common.db.sqlalchemy import db
import traceback

from src.apps.hello.services import HelloService

class HelloView(views.MethodView):
    """
    """
    service = HelloService()

    def get(self):
        """
        hello
        """
        try:
            data = self.service.hello()
            return JsonResponse(message='success', data=data)
        except Exception as e:
            traceback.print_exc()
            abort(400, 'fail:' + str(e))
            
