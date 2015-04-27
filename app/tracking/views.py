from flask import Blueprint, render_template

mod = Blueprint('tracking', __name__)

@mod.route('/')
@mod.route('/index')
def index():
    return render_template('tracking/index.html')