from flask import jsonify, redirect, url_for, Blueprint, request, session, render_template
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from ..auth.models import User, Books
import requests

books_api = Blueprint('books_api', __name__)

COUNT=20
BASE_URL = "https://www.googleapis.com/books/v1/volumes?maxResults={}".format(COUNT)

@books_api.get('')
@login_required
def browse():
    url = "&q=multiverse"
    if "search" in request.args and request.args["search"] != "":
        url = "&q={}".format(request.args["search"])
    if "author" in request.args and request.args["author"] != "":
        if "search" in request.args and request.args["search"] == "":
            url = "&q="

        url += "+inauthor:{}".format(request.args["author"])

    if "page" in request.args:
        url += "&startIndex={}".format(COUNT*(int(request.args["page"])-1))

    try:
        r = requests.get(BASE_URL + url)
        if r.status_code == 200:
            books = r.json()
            return books, 200
        else:
            return jsonify(error="Something Went Wrong! Please Try Again"), 400
    except Exception as e:
        return jsonify(error="Something Went Wrong! Please Try Again"), 400
