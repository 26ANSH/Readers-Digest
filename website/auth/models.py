from flask_login import UserMixin
from .. import db
   
bookshelf = db.Table('bookshelf',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('book_id', db.String, db.ForeignKey('books.id'), primary_key=True)
)

blogshelf = db.Table('blogshelf',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('blog_id', db.String, db.ForeignKey('blogs.id'), primary_key=True)
)
class User(UserMixin, db.Model):

    _tablename_ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable=False)
    lname = db.Column(db.String(10))
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(16), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    books = db.relationship('Books', secondary=bookshelf, lazy='subquery',
        backref=db.backref('user', lazy=True))
    
    blogs = db.relationship('Blogs', secondary=blogshelf, lazy='subquery',
        backref=db.backref('user', lazy=True))

    def _init_(self, fname, lname, email, password, admin=False):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.admin = True if admin else False

    def is_admin(self):
        """True if the user is an admin."""
        return self.admin
class Books(db.Model):

    _tablename_ = 'books'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    isbn = db.Column(db.String(10), nullable=False, unique=True)
    likes = db.Column(db.Integer, default=0)
class Blogs(db.Model):

    _tablename_ = 'blogs'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    link = db.Column(db.String(200), nullable=False, unique=True)
    likes = db.Column(db.Integer, default=0)