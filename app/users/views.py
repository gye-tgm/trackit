from app.users.forms import LoginForm
from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask.ext.login import login_user, login_required, logout_user

mod = Blueprint('users', __name__, template_folder='templates')


@mod.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user)
        flash("Login successful")
        return redirect(url_for('tracking.index'))
    return render_template('users/login.html', form=form)


@mod.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the ession->User connection for this session.
    logout_user()
    return redirect(url_for('tracking.index'))