from flask import jsonify, redirect, url_for, Blueprint, request, session, render_template
from flask_login import login_required, current_user

view = Blueprint('view', __name__)

@view.route('/')
def index():
    if current_user.is_authenticated:
        return redirect('/books')
    return render_template('main/landing.html')


