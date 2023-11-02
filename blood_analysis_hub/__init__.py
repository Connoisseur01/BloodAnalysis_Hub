from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7fea80b8940ff4a6e0cb55b70fd9849'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'

from blood_analysis_hub.users.routes import users
from blood_analysis_hub.posts.routes import posts
from blood_analysis_hub.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)