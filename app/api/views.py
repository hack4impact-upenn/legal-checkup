from flask import flash, jsonify, redirect, render_template, url_for
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
    print('is this working3232')
    if form.validate_on_submit():
    	print('is this working2')
        # parameters = []
        new_api = Api(
            name=form.name.data,
            region=form.region.data,
            description=form.description.data
        )
        db.session.add(new_api)
        try:
            db.session.commit()
            # print('hello')
            flash('API {} successfully added'
                      .format(new_api.name),
                      'form-success')
            return redirect(url_for('api.index'))
        except IntegrityError:
            db.session.rollback()
            flash('Database error occurred. Please try again.',
                  'form-error')
    print('is this working23')
    return render_template('api/add.html', form=form)



@api.route('/info/<int:api_id>', methods=['GET'])
# @login_required
def get_api_info(api_id):
    id = Api.query.get_or_404(api_id)
    return jsonify({'name': id.name, 'region': id.region, 'description' : id.description})
