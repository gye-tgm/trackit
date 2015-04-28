from app import db
from app.data import CRUDMixin
from app.models import User
from app.models.celebrity import Celebrity


class Follow(db.Model, CRUDMixin):
    """
    Defines the relationship between these two classes without having additional attributes in neither of them!
    """
    __tablename__ = 'follow'
    celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    following_since = db.Column(db.Date, nullable=False, default=db.func.now())

    celebrity = db.relationship(Celebrity, backref="follows")
    user = db.relationship(User, backref="follows")