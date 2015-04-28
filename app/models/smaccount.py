from app import db
from app.data import CRUDMixin


class SocialMediaAccount(db.Model, CRUDMixin):
    __tablename__ = 'smaccount'
    celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))