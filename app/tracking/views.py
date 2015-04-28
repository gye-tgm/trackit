from app.models import TwitterAccount, FacebookAccount
from app.tracking.forms import AddFbForm, AddTwitterForm
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask.ext.login import login_required
from flask.ext import login

mod = Blueprint('tracking', __name__)

@mod.route('/', methods=['GET', 'POST'])
@mod.route('/index/', methods=['GET', 'POST'])
@login_required
def index():
    fbform = AddFbForm(request.form)
    twform = AddTwitterForm(request.form)

    if twform.validate_on_submit():
        acc = TwitterAccount(username=twform.username.data)
        u = login.current_user
        u.accounts.append(acc)
        u.save()
        flash("Twitter acount added!")
        return redirect(url_for("tracking.index"))

    if fbform.validate_on_submit():
        acc = FacebookAccount(url=fbform.url.data)
        u = login.current_user
        u.accounts.append(acc)
        u.save()
        flash("Facebook acount added!")
        return redirect(url_for("tracking.index"))

    return render_template('tracking/index.html', fbform=fbform, twform=twform)