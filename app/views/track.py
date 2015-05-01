from app.models import User
from flask import Blueprint, render_template
from flask.ext.login import login_required, current_user

mod = Blueprint('track', __name__)

@mod.route('/user/<string:username>')
def user(username):
    u = User.query.filter_by(username=username).first_or_404()
    return render_template('track/user.html', posts=list(u.posts), username=u.username)

@mod.route('/me')
@login_required
def me():
    return user(current_user.username)

@mod.route('/following')
@login_required
def following():
    return render_template('404.html')

@mod.route('/')
def index():
    return render_template('track/index.html')