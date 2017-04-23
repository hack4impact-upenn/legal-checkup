from flask import flash, redirect, render_template
from ..models import EditableHTML

from . import api

@api.route('/index')
def index():
    """View all apis."""
    return render_template('api/index.html')

@api.route('/info/<int:api_id>', methods=['GET']) 
# @login_required 
def get_api_info(api_id): 
	id = Api.query.get_or_404(api_id) 
	return jsonify({'name': id.name, 'region': id.region, 'description' : id.description}) 

