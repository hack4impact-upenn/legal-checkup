from flask_wtf import Form
from wtforms.fields import (
    SubmitField,
    TextField
)
from wtforms.validators import InputRequired, Length

class ParameterForm(Form):
    name = TextField('Parameter Name', validators=[InputRequired(), Length(1, 500)])
    param_format = TextField('Format', validators=[InputRequired(), Length(1, 500)])
    submit = SubmitField('Add Parameter')
