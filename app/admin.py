from app import adm, db
from app.models import User, Follow, SocialMediaAccount, FacebookAccount, TwitterAccount
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()


# adm.add_view(AuthenticatedModelView(User, db.session))
adm.add_view(AuthenticatedModelView(Follow, db.session))
adm.add_view(AuthenticatedModelView(SocialMediaAccount, db.session))
adm.add_view(AuthenticatedModelView(FacebookAccount, db.session))
adm.add_view(AuthenticatedModelView(TwitterAccount, db.session))