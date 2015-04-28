from app import db
from app.models import User
db.create_all()

User.create(username='admin', password='admin', role=1)
User.create(username='gary', password='password', role=0)
