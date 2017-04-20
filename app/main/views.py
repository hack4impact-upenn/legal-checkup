from flask import render_template, flash
from flask.ext.login import login_required, admin_required
from ..models import EditableHTML, Api
from sqlalchemy.exc import IntegrityError
from forms import NewApiForm
from .. import db
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


@admin.route('/api/add_api', methods=['GET','POST'])
@login_required
def new_api():
	form = NewApiForm()
    if form.validate_on_submit():
    	api = Api(
            id=form.api_id.data,
            name=form.name.data,
            region=form.region.data,
            description=form.description.data,
            parameters=form.parameters.data
        )
        if Api.query.filter(Api.name == form.name.data).first() \
                is not None:
            flash('Api {} already exists.'.format(api.name),
                  'form-error')
        else:
            db.session.add(api)
            try:
                db.session.commit()
                flash('Api {} successfully created'
                      .format(api.name),
                      'form-success')
                return render_template('page.html'), 200
            except IntegrityError:
                db.session.rollback()
                flash('Database error occurred. Please try again.',
                      'form-error')
    return render_template('page.html'), 200