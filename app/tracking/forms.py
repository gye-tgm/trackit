from flask.ext.wtf import Form
from wtforms import StringField, SubmitField


class AddTwitterForm(Form):
    username = StringField('Twitter Username')
    submit = SubmitField('Submit')


class AddFbForm(Form):
    url = StringField('Facebook URL')
    submit = SubmitField('Submit')

