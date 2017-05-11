from flask_wtf import Form
from wtforms.fields import (
    BooleanField,
    FieldList,
    FormField,
    SelectField,
    SubmitField,
    TextAreaField,
    TextField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import InputRequired, Length

from ..models import Parameter
from .. import db

class ParameterForm(Form):
    name = TextField('Parameter Name', validators=[InputRequired(), Length(1, 500)])
    description = TextField('Description', validators=[InputRequired(), Length(1, 500)])

class NewAPIForm(Form):
    name = TextField('Name of API', validators=[InputRequired(), Length(1, 500)])
    region = SelectField('Region',
                            choices=[('Philadelphia', 'Philadelphia'), ('Pennsylvania', 'Pennsylvania')],
                            validators=[InputRequired()]
                            )
    parameters = QuerySelectMultipleField('Parameters',
                            validators=[InputRequired()],
                            query_factory=lambda: db.session.query(Parameter).
                            order_by('name'),
                            get_label='name'
                            )
    description= TextAreaField('Description')
    submit = SubmitField('Add API')
