from flask import Blueprint

api = Blueprint('api', __name__)

from . import views  # noqa
from . import forms  # noqa
