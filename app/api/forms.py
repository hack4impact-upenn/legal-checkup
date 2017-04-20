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
    name = TextField('Paramater Name', validators=[InputRequired(), Length(1, 500)])
    param_type = SelectField('Parameter Type',
                                choices=[('String, String'), ('Boolean, Boolean')],
                                validators=[InputRequired()]
                                )
    description = TextField('Description', validators=[InputRequired(), Length(1, 500)])

class NewAPIForm(Form):
    name = TextField('Name of API', validators=[InputRequired(), Length(1, 500)])
    region = SelectField('Region',
                            choices=[('Philadelphia', 'Philadelphia'), ('Pennsylvania', 'Pennsylvania')],
                            validators=[InputRequired()]
                            )
    parameters = SelectMultipleField('Parameters',
                            choices=[('Philadelphia', 'Philadelphia'), ('Pennsylvania', 'Pennsylvania')],
                            validators=[InputRequired()]
                            )
    params = FieldList(FormField(ParameterForm))
    is_searchable = BooleanField('Searchable')
    description= TextAreaField('Description')
    submit = SubmitField('Add API')
