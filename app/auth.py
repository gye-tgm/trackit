from app.models.users import User
from app import lm

# using /user/login if the user has not logged in yet
lm.login_view = 'users.login'

@lm.user_loader
def load_user(userid):
    print(userid)
    return User.get(userid)
    return User.query.filter_by(username=userid).one()
