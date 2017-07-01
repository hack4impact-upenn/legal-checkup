import requests
from flask import render_template, flash, request, jsonify, redirect, url_for
from ..models import EditableHTML, Api
from . import request
from .forms import (SearchForm, ParamsForm)

from wtforms.fields import (BooleanField, PasswordField, StringField,
                            SubmitField)

@request.route('/search', methods=['GET', 'POST'])
def searchForApi():
    """Search for an API"""
    searchForm = SearchForm()
    if searchForm.validate_on_submit():
        apiName = searchForm.api.data
        # Api.query.filter_by(name=name) # TODO: get params from db
        return redirect(url_for('request.searchData'))
    return render_template('api/search.html', form=searchForm)


@request.route('/search_params', methods=['GET', 'POST'])
def searchData():
    apiName = SearchForm().api.data
    params = [
        {'name': "s", 'param_format': "String"},
        {'name': "y", 'param_format': "Year"}
        ]

    paramForm = ParamsForm()
    for param in params:
        field = StringField(param['name'])
        setattr(ParamsForm, param['name'], field)

    if paramForm.validate_on_submit():
        url = 'http://www.omdbapi.com/'
        #TODO: get url from db
        paramData = {}
        for param in params:
            pName = param['name']
            paramData[pName] = paramForm[pName].data

        r = requests.get(url, params=paramData)
        data = r.content
        # print(data
        # for key in data:
            # print(data[key])
        return render_template('api/search_data.html', data=data)
    return render_template('api/search_params.html', form=paramForm, params=params, apiName = apiName)
