from flask_login import UserMixin
from. import db

class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable=False)
    lname = db.Column(db.String(10))
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(16), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, fname, lname, email, password, admin=False):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.admin = True if admin else False

    def is_admin(self):
        """True if the user is an admin."""
        return self.admin