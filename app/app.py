from threading import Thread
import time
from app.crawling.twitter import TwitterCrawler
from app.models import User, ROLE_ADMIN, Follow, SocialMediaAccount, Post, TwitterPost
from app.models.facebook.account import FacebookAccount
from app.models.twitter.account import TwitterAccount
from flask import Flask, render_template
from app.extensions import db, login_manager, twitter_api, admin
from app.views.track import mod as track_mod
from app.views.user import mod as user_mod
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login
from flask_bootstrap import Bootstrap
import schedule
import tweepy


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    configure_app(app, config_object)
    configure_hook(app)
    configure_blueprints(app)
    configure_extensions(app)
    configure_error_handlers(app)
    return app


def configure_app(app, config_object):
    app.config.from_object(config_object)


def configure_extensions(app):
    # http://stackoverflow.com/questions/19437883/when-scattering-flask-models-runtimeerror-application-not-registered-on-db-w
    db.app = app
    db.init_app(app)

    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(id):
        return User.get(int(id))
    login_manager.init_app(app)

    class AuthenticatedModelView(ModelView):
        def is_accessible(self):
            return login.current_user.is_authenticated() and login.current_user.role == ROLE_ADMIN

    admin.add_view(AuthenticatedModelView(User, db.session, endpoint='myuser'))
    admin.add_view(AuthenticatedModelView(Follow, db.session))
    admin.add_view(AuthenticatedModelView(SocialMediaAccount, db.session))
    admin.add_view(AuthenticatedModelView(FacebookAccount, db.session))
    admin.add_view(AuthenticatedModelView(TwitterAccount, db.session))
    admin.add_view(AuthenticatedModelView(Post, db.session))
    admin.add_view(AuthenticatedModelView(TwitterPost, db.session))
    admin.init_app(app)

    Bootstrap(app)

    twitter_api.auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'],
                                           app.config['CONSUMER_SECRET'])
    twitter_api.auth.set_access_token(app.config['ACCESS_TOKEN'],
                                      app.config['ACCESS_TOKEN_SECRET'])


def configure_hook(app):
    twcr = TwitterCrawler()

    def run_schedule():
        while 1:
            schedule.run_pending()
            time.sleep(1)

    @app.before_request
    def before_request():
        # we shouldn't query so often...
        # https://dev.twitter.com/rest/public/rate-limiting
        schedule.every(1).minute.do(twcr.crawl_all)
        t = Thread(target=run_schedule)
        t.start()


def configure_blueprints(app):
    app.register_blueprint(track_mod, url_prefix='/track')
    app.register_blueprint(user_mod, url_prefix='/user')


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500