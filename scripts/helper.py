from app import create_app
from app.extensions import db
from app.models import User

app = create_app('config.BaseConfiguration')
db.create_all()

User.create(username='admin', password='admin', role=1)
User.create(username='gary', password='password', role=0)