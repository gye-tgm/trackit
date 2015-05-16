from app import create_app
from app.config import BaseConfiguration
from app.extensions import db
from app.models import User, TwitterPost

app = create_app(BaseConfiguration)
db.create_all()

User.create(username='admin', password='admin', role=1)
User.create(username='gary', password='password', role=0)
TwitterPost.create()
