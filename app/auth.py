from flask.ext.login import LoginManager
from app.models.users import User

lm = LoginManager()
lm.login_view = 'users.login'

@lm.user_loader
def load_user(user_id):
    return User.get(user_id)