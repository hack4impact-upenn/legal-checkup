from flask import render_template
from ..models import EditableHTML

from . import main


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template('main/about.html',
                           editable_html_obj=editable_html_obj)

@admin.route('/api/<int:api_id>/info', methods=['GET'])
@login_required
def get_api_info(api_id):
    id = models.Api.query.get_or_404(api_id)
    return jsonify({'description' : id.description})