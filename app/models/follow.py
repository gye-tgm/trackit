from app.extensions import db
from app.data import CRUDMixin
from app.models import User


class Follow(db.Model, CRUDMixin):
    """
    a follows b
    """
    __tablename__ = 'follow'
    a_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    b_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    following_since = db.Column(db.Date, default=db.func.now())

    # issue: http://stackoverflow.com/questions/18807322/sqlalchemy-foreign-key-relationship-attributes
    b = db.relationship(User, backref="follow_assoc", foreign_keys="Follow.b_id")
