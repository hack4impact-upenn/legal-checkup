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
    name = TextField('Parameter Name', validators=[InputRequired(), Length(1, 500)])
    description = TextField('Description', validators=[InputRequired(), Length(1, 500)])

class NewAPIForm(Form):
    name = TextField('Name of API', validators=[InputRequired(), Length(1, 500)])
    region = SelectField('Region',
                            choices=[('Philadelphia', 'Philadelphia'), ('Pennsylvania', 'Pennsylvania')],
                            validators=[InputRequired()]
                            )
    parameters = SelectMultipleField('Parameters',
                            choices=[('Name', 'Name'), ('Date of Birth', 'Date of Birth')],
                            validators=[InputRequired()]
                            )
    url = TextField('API URL', validators=[InputRequired(), Length(1, 500)])
    description= TextAreaField('Description')
    submit = SubmitField('Add API')
