from app.extensions import db
from app.models import SocialMediaAccount


class TwitterAccount(SocialMediaAccount):
    __tablename__ = 'tw_account'
    __mapper_args__ = {'polymorphic_identity': 'tw_account'}

    id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    username = db.Column(db.String)