from app.models import User
from flask import Blueprint, render_template
from flask.ext.login import login_required, current_user

mod = Blueprint('post', __name__)

@mod.route('/search/<string:username>')
@login_required
def user(username):
    u = User.query.filter_by(username=username).first_or_404()
    return render_template('post/user.html', posts=list(u.posts), username=u.username)

@mod.route('/me')
def me():
    return user(current_user.username)

@mod.route('/others')
@login_required
def others():
    pass