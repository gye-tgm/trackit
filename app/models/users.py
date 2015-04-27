from app.data import CRUDMixin, db
from flask.ext.login import UserMixin
from sqlalchemy import Column, String


class User(db.Model, UserMixin, CRUDMixin):
    __tablename__ = 'users'

    username = Column(String, unique=True)
    password = Column(String)

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