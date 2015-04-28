from app.data import CRUDMixin, db
from app.models import SocialMediaAccount
from flask.ext.login import UserMixin


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin, CRUDMixin):
    __tablename__ = 'user'

    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.Integer, default=ROLE_USER)

    accounts = db.relationship(SocialMediaAccount, backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_valid_password(self, password):
        # normally you would compare the hash here
        return self.password == password

    def __repr__(self):
        return "<User #{:d}>".format(self.id)