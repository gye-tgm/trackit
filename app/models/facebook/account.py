from app.extensions import db
from app.models import SocialMediaAccount


class FacebookAccount(SocialMediaAccount):
    __tablename__ = 'fb_account'
    __mapper_args__ = {'polymorphic_identity': 'fb_account'}

    id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    url = db.Column(db.String)