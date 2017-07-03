from flask import flash, jsonify, redirect, render_template, url_for
from ..models import EditableHTML, Api, ApiParameterLink, Parameter

from flask_login import login_required
from sqlalchemy.exc import IntegrityError
from wtforms.fields import SelectField
from flask_wtf.file import InputRequired
import requests

from .forms import (
    NewAPIForm,
    ParameterForm
)

from .. import db
from . import api

@api.route('/')
def index():
    """View all apis."""
    apis = Api.query.all()
    return render_template('api/index.html', apis=apis)


@api.route('/add', methods=['GET', 'POST'])
def add_api():
    """Create a new API."""
    form = NewAPIForm()
    if form.validate_on_submit():
        new_api = Api(
            name=form.name.data,
            region=form.region.data,
            description=form.description.data,
            url=form.url.data
        )
        db.session.add(new_api)
        try:
            db.session.commit()
            flash('API {} successfully added'
                      .format(new_api.name),
                      'form-success')
            return redirect(url_for('api.index'))
        except IntegrityError:
            db.session.rollback()
            flash('Database error occurred. Please try again.',
                  'form-error')
    return render_template('api/add.html', form=form)

@api.route('/info', methods=['GET'])
def get_api_info_all():
    apis = Api.query.all()
    apis_to_jsonify = []
    for api in apis:
        apis_to_jsonify.append({
            'name': api.name,
            'region': api.region,
            'description': api.description,
            'url': api.url})
    return jsonify({'APIs': apis_to_jsonify})

@api.route('/info/<int:api_id>', methods=['GET'])
def get_api_info(api_id):
    id = Api.query.get_or_404(api_id)
    return jsonify({'name': id.name, 'region': id.region, 'description' : id.description, 'url': id.url})


@api.route('/request/<string:api_name>', methods=['GET'])
def get_api_name(api_name):
    url = Api.query.get_or_404(api_name)
    r = request.head(url)
    if r.status_code != 200:
        return render_template('api/requests.html')
    return redirect(url_for('api.name'))
