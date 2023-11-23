from sqlalchemy import CheckConstraint
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, CheckConstraint('age >= 0 AND age <= 120'), nullable=True)
    gender = db.Column(db.Enum('male', 'female', 'other', name='gender_enum'), nullable=True)
    tests = db.relationship('Test', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, username, email, password, age=None, gender=None):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    attributes = db.relationship('Attribute_list', backref='test', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"Test('{self.title}', '{self.date_posted}')"
    
class Attribute_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'), nullable=False)
    value = db.Column(db.Numeric(scale=2), nullable=False)
    
    def __repr__(self):
        return f"Attribute('{self.attribute_id}', '{self.value}')"
    

class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    min_male = db.Column(db.Numeric(scale=2), nullable=False)
    max_male = db.Column(db.Numeric(scale=2), nullable=False)
    min_female = db.Column(db.Numeric(scale=2), nullable=False)
    max_female = db.Column(db.Numeric(scale=2), nullable=False)
    desc_over = db.Column(db.String(500), nullable=False)
    desc_under = db.Column(db.String(500), nullable=False)
