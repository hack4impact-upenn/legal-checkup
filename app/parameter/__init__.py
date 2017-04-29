from flask import Blueprint

parameter = Blueprint('parameter', __name__)

from . import forms, views
