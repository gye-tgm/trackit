from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask.ext.admin import Admin
admin = Admin()

import tweepy
twitter_api = tweepy.API()