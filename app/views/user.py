from app.forms.user import RegisterForm, LoginForm, AddAccForm, AddFbForm, AddTwitterForm
from app.models import TwitterAccount, FacebookAccount, Follow
from flask.ext import login as flask_login

from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask.ext.login import login_user, login_required, logout_user

from app.models import User


mod = Blueprint('user', __name__, template_folder='templates')


@mod.route('/')
def index():
    return render_template('user/index.html')


@mod.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user)
        flash("Login successful", category="info")
        return redirect(request.args.get("next") or url_for('.index'))
    return render_template('user/login.html', form=form)


@mod.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@mod.route('/register/', methods=("POST", "GET"))
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.create(username=form.name.data,
                           password=form.password.data)
        flash("Registration successful", category="success")
        return redirect(url_for(".index"))
    return render_template('user/register.html', form=form)

# TODO: /settings or /settings/
@mod.route('/settings/', methods=['GET', 'POST'])
@login_required
def settings():
    fbform = AddFbForm(request.form)
    twform = AddTwitterForm(request.form)
    accform = AddAccForm(request.form)

    u = flask_login.current_user

    if twform.validate_on_submit():
        acc = TwitterAccount(username=twform.twacc.data)
        u.accounts.append(acc)
        u.save()
        flash("Twitter acount added!", "success")
        return redirect(url_for(".settings"))

    if fbform.validate_on_submit():
        acc = FacebookAccount(url=fbform.fburl.data)
        u.accounts.append(acc)
        u.save()
        flash("Facebook acount added!", "success")
        return redirect(url_for(".settings"))

    if accform.validate_on_submit():
        print(accform.user)
        print(u.following)
        # http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#association-object
        f = Follow(a_id=u.id, b_id=accform.user.id)
        f.a = u
        f.b = accform.user
        f.save()

        flash("You follow " + accform.user.username + " now", "success")
        return redirect(url_for(".settings"))

    twaccounts = u.get_twitter_accounts()
    fbaccounts = u.get_facebook_accounts()

    return render_template('user/settings.html', fbform=fbform, twform=twform, twaccounts=twaccounts,
                           fbaccounts=fbaccounts, accform=accform, following=u.get_following(),
                           followers=u.get_followers())