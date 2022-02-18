import sys
import os
import logging
from flask_script import Manager
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from gevent import monkey
from gevent.pywsgi import WSGIServer

# monkey.patch_all()

from src.common.db.sqlalchemy import db
from src.middlewares.handlers import *

# init_admin()

BASE_DIR = os.getcwd()
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# sys.path.append(os.path.join(BASE_DIR, 'plugins'))
sys.path.insert(0, os.path.join(BASE_DIR, 'plugins'))

# logger = logging.getLogger('debug')

manager = Manager(app)

CORS(app, supports_credentials=True)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    logging.debug("Started")
    manager.run()
    
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()
