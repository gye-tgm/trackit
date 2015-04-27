from app.auth import load_user
from app.users.forms import LoginForm
from flask import Blueprint, flash, redirect, url_for, render_template
from flask.ext.login import login_user

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Login successful")
        return redirect(url_for('users.index'))
    return render_template('users/login.html', form=form)


 # @mod.route('/login/', methods=['GET', 'POST'])
 #    def login():
 #      """
 #      Login form
 #      """
 #      form = LoginForm(request.form)
 #      # make sure data are valid, but doesn't validate password is right
 #      if form.validate_on_submit():
 #        user = User.query.filter_by(email=form.email.data).first()
 #        # we use werzeug to validate user's password
 #        if user and check_password_hash(user.password, form.password.data):
 #          # the session can't be modified as it's signed,
 #          # it's a safe place to store the user id
 #          session['user_id'] = user.id
 #          flash('Welcome %s' % user.name)
 #          return redirect(url_for('users.home'))
 #        flash('Wrong email or password', 'error-message')
 #      return render_template("users/login.html", form=form)