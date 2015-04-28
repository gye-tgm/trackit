from app.models import TwitterAccount
from app.tracking.forms import AddFbForm, AddTwitterForm
from flask import Blueprint, render_template, request
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
        u = login.current_user
        acc = TwitterAccount(username=twform.username.data)
        u.accounts.append(acc)
        u.save()

    if fbform.validate_on_submit():
        pass

    return render_template('tracking/index.html', fbform=fbform, twform=twform)