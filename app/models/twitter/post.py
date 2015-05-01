from app.extensions import db
from app.data import CRUDMixin
from app.models import Post


class TwitterPost(Post, CRUDMixin):
    __tablename__ = 'twitterpost'
    __mapper_args__ = {'polymorphic_identity': 'tw_post'}

    id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tw_id = db.Column(db.Integer, unique=True)