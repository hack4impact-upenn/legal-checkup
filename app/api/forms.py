from flask_wtf import Form
from wtforms.fields import (
    BooleanField,
    FieldList,
    FormField,
    SelectField,
    SelectMultipleField,
    SubmitField,
    TextAreaField,
    TextField
)
from wtforms.validators import InputRequired, Length

class ParameterForm(Form):
    param_name = TextField('Parameter Name', validators=[InputRequired(), Length(1, 500)])
    description = TextField('Description', validators=[InputRequired(), Length(1, 500)])
    param_format = TextField('Format', validators=[InputRequired(), Length(1, 500)])

class NewAPIForm(Form):
    name = TextField('Name of API', validators=[InputRequired(), Length(1, 500)])
    region = SelectField('Region',
                            choices=[('Philadelphia', 'Philadelphia'), ('Pennsylvania', 'Pennsylvania')],
                            validators=[InputRequired()]
                            )
    # Parameters are dynamically populated when rendered -- see views.py.
    parameters = SelectMultipleField('Parameters',
                            choices=[],
                            validators=[InputRequired()])
    # TODO: Removing parameters
    new_parameter = FieldList(FormField(ParameterForm), min_entries=0)
    add_parameter = SubmitField('Add a new parameter')
    url = TextField('API URL', validators=[InputRequired(), Length(1, 500)])
    description= TextAreaField('Description')
    submit = SubmitField('Add API')
