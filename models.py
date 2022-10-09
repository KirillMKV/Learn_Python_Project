from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(), index = True)
    last_name = db.Column(db.String(), index = True)
    password = db.Column(db.String(10))
    role = db.Column(db.String(10), index=True)
    
    def self_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Items(db.Model):
    id = db.Column(db.Integer)
    item_code = db.Column(db.Integer, unique= True, primary_key = True)
    name = db.Column(db.String, index = True, unique= True)
    price = db.Column(db.Integer, index = True)
    url = db.Column(db.String, index = True, unique= True)
    
    def __repr__(self):
        return '<Item {}>'.format(self.name)
