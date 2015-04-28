from app import db
from app.data import CRUDMixin


class SocialMediaAccount(db.Model, CRUDMixin):
    __tablename__ = 'smaccount'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    discriminator = db.Column(db.Integer)
    __mapper_args__ = {'polymorphic_on': discriminator}