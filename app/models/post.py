from app import db
from app.data import CRUDMixin


class Post(db.Model, CRUDMixin):
    __tablename__ = 'post'

    content = db.Column(db.String)
    time = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))