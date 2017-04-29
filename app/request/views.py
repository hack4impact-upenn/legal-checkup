import requests
from flask import render_template, flash, request, jsonify
from ..models import EditableHTML, Api
from . import request
from .forms import (SearchForm, ParamsForm)

from wtforms.fields import (BooleanField, PasswordField, StringField,
                            SubmitField)

@request.route('/search', methods=['GET', 'POST'])
def searchForApi():
    """Search for an API"""
    form = SearchForm()
    if form.validate_on_submit():
        name = form.api.data
        # Api.query.filter_by(name=name) #
        print("AHOY")
        params = [
            {'name': "name1", 'param_format': "format1"},
            {'name': "name2", 'param_format': "format2"}
            ]
        form = ParamsForm()#params)
        for param in params:
            field = StringField(param['name'])
            setattr(ParamsForm, param['name'], field)

        return render_template('api/search_params.html', form=form, params=params)
    return render_template('api/search.html', form=form)


@request.route('/')
def index():
    return render_template('api/search.html')

# @request.route('/search_params', methods=['GET', 'POST'])
# def getApiParams(api_id):
#     id = Api.query.get(api_id)
#     params = Api.query.get_params(api_id)
#
#     form = ParamsForm(params)
#
#     for param in params:
#         name = param.name
#         param_format = param.param_format
#         # TODO: make a form for the user to fill out
#     return render_template('api/search_params.html', params=params)
