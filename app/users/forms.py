from app.models import User
from flask.ext.wtf import Form
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import InputRequired


class LoginForm(Form):
    name = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

    def validate_password(form, field):
        try:
            user = User.query.filter(User.username == form.name.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")

        form.user = user