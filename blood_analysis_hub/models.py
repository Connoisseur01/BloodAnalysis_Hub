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
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, CheckConstraint('age >= 0 AND age <= 120'), nullable=True)
    gender = db.Column(db.Enum('male', 'female', 'other', name='gender_enum'), nullable=True)
    tests = db.relationship('Test', backref='author', lazy=True)
    
    def __init__(self, username, email, password, age=None, gender=None):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Complete blood count (CBC)
    # Red blood cells
    hb = db.Column(db.Numeric(precision=2), nullable=False) # Heamoglobin [g/L]
    hct = db.Column(db.Integer, CheckConstraint('hct >= 0 AND hct <= 100'), nullable=False) # Haematoglobin [%]
    rbc = db.Column(db.Integer, nullable=False) # Red Blood Cell Count [cells/L]
    # Red blood cell indices
    mcv = db.Column(db.Numeric(precision=2), nullable=False) # Mean Corpuscular Volume [fL]
    mch = db.Column(db.Numeric(precision=2), nullable=False) # Mean Corpuscular Hemoglobin [pg]
    mchc = db.Column(db.Numeric(precision=2), nullable=False) # Mean Corpuscular Hemoglobin Concentration [g/L]
    # white blood cells
    wbc = db.Column(db.Integer, nullable=False) # White Blood Cell Count [cells/L]
    # Platelets
    pc = db.Column(db.Integer, nullable=False) # Platelet Count [cells/L]
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Test('{self.title}', '{self.date_posted}')"