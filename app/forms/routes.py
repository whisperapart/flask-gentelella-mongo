from app.forms import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')
