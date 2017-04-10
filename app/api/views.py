from flask import render_template
from ..models import EditableHTML

from . import api

@api.route('/')
# @login_required
def index():
    """View all apis."""
    return render_template('api/index.html')

@api.route('/add')
# @login_required
def add_api():
    return render_template('api/add.html')
