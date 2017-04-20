from flask.ext.wtf import Form
from wtforms.fields import (IntegerField, StringField, SelectField)
from wtforms.validators import InputRequired

class NewApiForm(Form):
	api_id = IntegerField(
		'id', validators=[InputRequired()])
	name = StringField(
		'name', validators=[InputRequired(), Length(1, 64)])
	region = StringField(
		'region', validators=[InputRequired(), Length(1, 64)])
	description = StringField(
		'description', validators=[InputRequired(), Length(1, 128)])
	parameters = SelectField(
		'parameters', coerce=int)