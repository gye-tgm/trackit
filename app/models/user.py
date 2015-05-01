from app.data import CRUDMixin
from app.extensions import db
from app.models.account import SocialMediaAccount
from app.models.facebook.account import FacebookAccount
from app.models.post import Post
from app.models.twitter.account import TwitterAccount
from flask.ext.login import UserMixin


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin, CRUDMixin):
    __tablename__ = 'user'

    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.Integer, default=ROLE_USER)

    accounts = db.relationship(SocialMediaAccount, backref='user', lazy='dynamic')
    posts = db.relationship(Post, backref='user', lazy='dynamic')

    following = db.relationship('Follow', backref="follower", foreign_keys='Follow.a_id')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def get_following(self):
        return [f.b for f in self.following]

    def get_followers(self):
        return [f.follower for f in self.follow_assoc]

    def is_valid_password(self, password):
        # normally you would compare the hash here
        return self.password == password

    def get_twitter_accounts(self):
        return list(filter(lambda x: isinstance(x, TwitterAccount), self.accounts))

    def get_facebook_accounts(self):
        return list(filter(lambda x: isinstance(x, FacebookAccount), self.accounts))

    def __repr__(self):
        return "<User #{:d}>".format(self.id)