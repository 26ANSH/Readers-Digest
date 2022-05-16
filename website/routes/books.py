from flask import jsonify, redirect, url_for, Blueprint, request, session, render_template
from flask_login import login_required, current_user
from ..api.books import book_details

books = Blueprint('books', __name__)

@books.route('/')
def hello():
    return redirect(url_for('books.browse_books'))

@books.route('/favs')
def fav_books():
    currentRoute = f'{request.url_rule.rule.split("/")[1]}-{request.url_rule.rule.split("/")[2]}'    
    return render_template('books/favs.html', user=current_user, currentRoute=currentRoute)

@books.route('/browse')
@login_required
def browse_books():
    currentRoute = f'{request.url_rule.rule.split("/")[1]}-{request.url_rule.rule.split("/")[2]}'    
    return render_template('books/browse.html', user=current_user, currentRoute=currentRoute)

@books.route('/<id>')
@login_required
def view_book(id):

    currentRoute = f'{request.url_rule.rule.split("/")[1]}-{request.url_rule.rule.split("/")[2]}'

    book = book_details(id)

    if book["status"]:
        return render_template('books/book.html', user=current_user, currentRoute=currentRoute, book=book["result"])
    else:
        return render_template('books/book.html', user=current_user, currentRoute=currentRoute, error=book["result"])

