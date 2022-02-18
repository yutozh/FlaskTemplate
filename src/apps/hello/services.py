import json
from src.common.http.response import JsonResponse, DataPackage
from src.common.db.sqlalchemy import db
from src.core.auth import make_jwt
from flask import request, abort, views, g
from src.conf.settings import settings
import logging

class HelloService:
    def hello(self):
        """
        hello
        """
        logging.info("OK")
        logging.warning("OK")
        return {"result": "Hello world"}
