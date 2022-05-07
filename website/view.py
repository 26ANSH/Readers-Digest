from flask import jsonify, redirect, url_for, Blueprint, request, session, render_template
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from . models import User

view = Blueprint('view', __name__)

@view.route('/')
def index():
    if current_user.is_authenticated:
        return "Hello, {}".format(current_user.fname)
    else:
        return "Hello, Guest"

@view.route('/profile')
@login_required
def profile():
    return render_template('user.html', user=current_user)

