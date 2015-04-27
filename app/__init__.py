from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
lm = LoginManager(app)

from app.default.views import mod as default_mod
app.register_blueprint(default_mod)

from app.users.views import mod as user_mod
app.register_blueprint(user_mod)

