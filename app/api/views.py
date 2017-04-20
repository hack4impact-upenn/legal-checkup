from flask import flash, redirect, render_template
from ..models import EditableHTML, Api, ApiParameterLink, Parameter

from flask_login import login_required
from sqlalchemy.exc import IntegrityError
from wtforms.fields import SelectField
from flask_wtf.file import InputRequired

from .forms import (
    NewAPIForm,
    ParameterForm
)

from .. import db
from . import api

@api.route('/')
# @login_required
def index():
    """View all apis."""
    return render_template('api/index.html')

@api.route('/add', methods=['GET', 'POST'])
# @login_required
def add_api():
    """Create a new API."""
    form = NewAPIForm()
    if form.validate_on_submit():
        parameters = []
        newAPI = Api(
            name=form.name.data,
            region=form.region.data,
            description=form.description.data,
            parameters=parameters
        )
        db.session.add(newAPI)
        try:
            db.session.commit()
            flash('API {} successfully added'
                      .format(newAPI.name),
                      'form-success')
            return redirect('api/index.html')
        except IntegrityError:
            db.session.rollback()
            flash('Database error occurred. Please try again.',
                  'form-error')
    return render_template('api/add.html', form=form)
