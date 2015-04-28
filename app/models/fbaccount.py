from app import db
from app.models import SocialMediaAccount


class FacebookAccount(SocialMediaAccount):
    __tablename__ = 'fbaccount'
    __mapper_args__ = {'polymorphic_identity': 'fb_account'}

    id = db.Column(db.Integer, db.ForeignKey('smaccount.id'), primary_key=True)
    url = db.Column(db.String)