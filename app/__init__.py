from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager(app)
from app import auth

from app.tracking.views import mod as tracking_mod
app.register_blueprint(tracking_mod, url_prefix='/tracking')

from app.users.views import mod as user_mod
app.register_blueprint(user_mod, url_prefix='/users')

from flask_bootstrap import Bootstrap
Bootstrap(app)