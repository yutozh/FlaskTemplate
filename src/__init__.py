from src.apps.hello.controllers import *
from flask_security import (
    LoginForm,
    url_for_security,
    SQLAlchemyUserDatastore,
    Security,
)
from src.common.app import app

hello_view = HelloView.as_view("sms")
app.add_url_rule("/hello", view_func=hello_view)
