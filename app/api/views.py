from flask import flash, redirect, render_template
from ..models import EditableHTML

from . import api

@api.route('/index')
def index():
    """View all apis."""
    return render_template('api/index.html')
