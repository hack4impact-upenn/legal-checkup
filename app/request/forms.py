from flask import url_for
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.fields import (BooleanField, PasswordField, StringField,
                            SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from ..models import Api

class SearchForm(Form):
    api = StringField('API', validators=[InputRequired()])
    submit = SubmitField('Search')

class ParamsForm(Form):
    api = StringField('API', validators=[InputRequired()])
    submit = SubmitField('Submit')
