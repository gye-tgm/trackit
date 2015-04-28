from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class AddTwitterForm(Form):
    username = StringField('Twitter Username', [InputRequired()])
    submit = SubmitField('Submit')


class AddFbForm(Form):
    url = StringField('Facebook URL', [InputRequired()])
    submit = SubmitField('Submit')

