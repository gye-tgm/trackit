from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager(app)
from app import auth

adm = Admin(app)
from app import admin

from app.tracking.views import mod as tracking_mod
app.register_blueprint(tracking_mod, url_prefix='/tracking')

from app.users.views import mod as user_mod
app.register_blueprint(user_mod, url_prefix='/users')

from flask_bootstrap import Bootstrap
Bootstrap(app)