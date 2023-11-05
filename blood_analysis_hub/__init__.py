from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blood_analysis_hub.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

CBC_REFERENCE = {
    'male': {
        'hb':{'min':2.09,'max':2.71},
        'hct':{'min':0.41,'max':0.53},
        'rbc':{'min':4.3,'max':5.9},
        'wbc':{'min':4.5,'max':11.0},
        'pc':{'min':150,'max':400},
        'mcv':{'min':80,'max':100},
        'mch':{'min':0.39,'max':0.54},
        'mchc':{'min':4.81,'max':5.58}
    },
    'female': {
        'hb':{'min':1.86,'max':2.48},
        'hct':{'min':0.36,'max':0.46},
        'rbc':{'min':3.5,'max':5.5},
        'wbc':{'min':4.5,'max':11.0},
        'pc':{'min':150,'max':400},
        'mcv':{'min':80,'max':100},
        'mch':{'min':0.39,'max':0.54},
        'mchc':{'min':4.81,'max':5.58}
    }
}

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from blood_analysis_hub.users.routes import users
    from blood_analysis_hub.tests.routes import tests
    from blood_analysis_hub.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(tests)
    app.register_blueprint(main)
    
    return app