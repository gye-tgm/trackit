from app import db
from app.data import CRUDMixin
from sqlalchemy import String
from sqlalchemy import Column


class Celebrity(db.Model, CRUDMixin):
    name = Column(String)
    accounts = db.relationship('SocialMediaAccount', backref='celebrity', lazy='dynamic')