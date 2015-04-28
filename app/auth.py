from app.models.users import User
from app import lm

# using /user/login if the user has not logged in yet
lm.login_view = 'user.login'

@lm.user_loader
def load_user(userid):
    return User.get(userid)
