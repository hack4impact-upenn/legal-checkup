from flask import flash, jsonify, redirect, render_template, request
from flask_login import login_required
from flask_restful import Resource, Api
from flask_wtf.file import InputRequired
from sqlalchemy.exc import IntegrityError
from wtforms.fields import SelectField

from ..models import EditableHTML, Parameter
from .forms import (
    ParameterForm
)

from .. import db
from . import parameter

@parameter.route('/')
def index():
    """View all parameters."""
    params = Parameter.query.all()
    return render_template('parameter/index.html', params=params)

@parameter.route('/add', methods=['GET', 'POST'])
def add():
    """Add parameter."""
    form = ParameterForm()
    if form.validate_on_submit():
        new_param = Parameter(
            name=form.name.data,
            param_format=form.param_format.data,
            count=0
        )
        db.session.add(new_param)
        try:
            db.session.commit()
            flash('Parameter successfully added',
                        'form-success')
            return redirect('parameter/')
        except IntegrityError:
            db.session.rollback()
            flash('Database error occurred. Please try again.',
                  'form-error')
    return render_template('parameter/add.html', form=form)

@parameter.route('/info/<int:param_id>', methods=['GET'])
def get_parameter_info(param_id):
    id = Parameter.query.get_or_404(param_id)
    return jsonify({'name': id.name, 'format': id.param_format, 'count': id.count})

@parameter.route('/info', methods=['GET'])
def get_parameter_info_all():
    params = Parameter.query.all()
    params_to_jsonify = []
    for param in params:
        params_to_jsonify.append({'name': param.name, 'format': param.param_format, 'count': param.count})
    return jsonify({'parameters': params_to_jsonify})


@parameter.route('/request/<string:param_name>', methods=['GET'])
def get_parameter_api(param_name):
    apis = Parameter.query.get_or_404(param_name)
    all_api_urls = []
    for api in apis:
        r = request.head(url)
        if r.status_code != 200:
            continue
        all_api_urls.append(url_for(api.id))
    return all_api_urls
