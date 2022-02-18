from flask import Flask
from dynaconf import FlaskDynaconf
from src.conf.settings import settings
import logging.config
from flask_babelex import Babel
from flask.logging import default_handler
import os

logging.config.dictConfig(settings.log)

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.logger.removeHandler(default_handler)

FlaskDynaconf(app, settings_files=settings.get('SETTINGS_FILE_FOR_DYNACONF'))

babel = Babel(app)