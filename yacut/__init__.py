import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)

BASE_DIR = os.path.dirname(app.instance_path)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
