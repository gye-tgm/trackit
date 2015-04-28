from app import db
from app.data import CRUDMixin
from app.models import SocialMediaAccount


class Celebrity(db.Model, CRUDMixin):
    __tablename__ = 'celebrity'

    name = db.Column(db.String)

    accounts = db.relationship(SocialMediaAccount, backref='celebrity', lazy='dynamic')