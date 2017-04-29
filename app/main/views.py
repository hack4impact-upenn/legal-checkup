from flask import render_template, flash
from flask_login import login_required
from ..models import EditableHTML, Api
from .. import db
from . import main


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/home')
def home():
    return render_template('main/home.html')

@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template('main/about.html', editable_html_obj=editable_html_obj)
