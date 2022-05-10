from flask import jsonify, redirect, url_for, Blueprint, request, session, render_template
from flask_login import login_required, current_user
import requests

books = Blueprint('books', __name__)

def book_details(id):
    url = f"https://www.googleapis.com/books/v1/volumes/{id}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            book = r.json()
            return {"result": book, "status": True}
        else:
            return {"result": f"There is no Book with ID: {id}", "status": False}
    except Exception:
        return {"result": "Something Went Wrong! Please Try Again", "status": False}

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
        return render_template('books/error.html', user=current_user, currentRoute=currentRoute, error=book["result"])

