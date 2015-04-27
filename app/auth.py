from flask.ext.login import LoginManager
from app.models.users import User
from app import lm

# using /user/login if the user has not logged in yet
lm.login_view = 'users.login'

@lm.user_loader
def load_user(user_id):
    return User.get(user_id)
