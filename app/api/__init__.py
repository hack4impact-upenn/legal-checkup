from flask import Blueprint

main = Blueprint('api', __name__)

from . import views  # noqa
