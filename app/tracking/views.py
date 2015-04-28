from flask import Blueprint, render_template
from flask.ext.login import login_required

mod = Blueprint('tracking', __name__)

@mod.route('/')
@mod.route('/index/')
@login_required
def index():
    return render_template('tracking/index.html')