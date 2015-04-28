from app import db
from app.models import SocialMediaAccount


class TwitterAccount(SocialMediaAccount):
    __tablename__ = 'twitteraccount'
    id = db.Column(db.Integer, db.ForeignKey('smaccount.id'), primary_key=True)
    username = db.Column(db.String)