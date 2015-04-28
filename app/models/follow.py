from app import db
from app.data import CRUDMixin
from app.models import User


class Follow(db.Model, CRUDMixin):
    """
    a follows b
    """
    __tablename__ = 'follow'
    a_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    b_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    following_since = db.Column(db.Date, nullable=False, default=db.func.now())

    # issue: http://stackoverflow.com/questions/18807322/sqlalchemy-foreign-key-relationship-attributes
    a = db.relationship(User, foreign_keys="Follow.a_id")
    b = db.relationship(User, foreign_keys="Follow.b_id")