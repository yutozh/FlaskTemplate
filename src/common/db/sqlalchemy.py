from flask_sqlalchemy import SQLAlchemy
from src.common.app import app

db = SQLAlchemy(app)