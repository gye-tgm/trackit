from app.models import User
from flask.ext.wtf import Form
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from wtforms import StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import InputRequired


class LoginForm(Form):
    name = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    submit = SubmitField('Login')

    # TODO: will validate_user be called before validate_password ?
    def validate_name(form, field):
        try:
            form.user = User.query.filter(User.username == form.name.data).one()
        except NoResultFound:
            raise ValidationError("User does not exist")

    def validate_password(form, field):
        if hasattr(form, 'user') and not form.user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")


class RegisterForm(Form):
    name = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    confirm = PasswordField('Confirm', [InputRequired()])
    submit = SubmitField('Register')

    def validate_password(form, field):
        if form.password.data != form.confirm.data:
            raise ValidationError("Passwords do not match")

    def validate_name(form, field):
        if User.query.filter(User.username == form.name.data).count() > 0:
            raise ValidationError("User already exists")