from flask import flash, jsonify, redirect, render_template
from ..models import EditableHTML, Api

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

# @api.route('/all-services', methods=['GET'])
# @login_required
# def get_all_apis():


# @api.route('/single-services', methods=['GET'])
# @login_required
# def get_single_api():


# @api.route('/input-by-parameter', methods=['GET'])
# @login_required
# def get_single_api():


# @api.route('/add-api', methods=['POST'])
# @login_required
# def add_api():
