from app.models import User
from app.users.forms import LoginForm, RegisterForm
from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask.ext.login import login_user, login_required, logout_user

mod = Blueprint('users', __name__, template_folder='templates')


@mod.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user)
        flash("Login successful")
        return redirect(request.args.get("next") or url_for('.index'))
    return render_template('users/login.html', form=form)


@mod.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the ession->User connection for this session.
    logout_user()
    return redirect(url_for('.index'))


@mod.route('/register/', methods=("POST", "GET"))
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.create(username=form.name.data,
                           password=form.password.data)
        flash("Registratoin successful")
        return redirect(url_for(".index"))
    return render_template('users/register.html', form=form)


@mod.route('/')
def index():
    return render_template('users/index.html')

@mod.route('/admin')
def admin():
    return render_template('users/admin.html')