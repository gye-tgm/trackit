from app import adm, db
from app.models import User
from flask.ext.admin.contrib.sqla import ModelView

adm.add_view(ModelView(User, db.session))