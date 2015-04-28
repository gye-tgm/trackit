from app import db
from app.data import CRUDMixin
from app.models import User
from app.models.celebrity import Celebrity
from sqlalchemy import func


class Follow(db.Model, CRUDMixin):
    """
    Defines the relationship between these two classes without having additional attributes in neither of them!
    """
    celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    following_since = db.Column(db.Date, nullable=False, default=func.now())

    celebrity = db.relationship(Celebrity, backref="follows")
    user = db.relationship(User, backref="follows")