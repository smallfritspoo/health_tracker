# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# local import
from config import app_config

# initialize sql-alchemy
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please login to access this page'
bootstrap = Bootstrap()

from flask import request, jsonify, abort


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name.strip()])
    app.config.from_pyfile('../config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.labs import bp as labs_bp
    app.register_blueprint(labs_bp, url_prefix='/labs')

    from app.bloodpressure import bp as bloodpressure_bp
    app.register_blueprint(bloodpressure_bp, url_prefix='/bloodpressure')

    from app.weight import bp as weight_bp
    app.register_blueprint(weight_bp, url_prefix='/weight')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from app import models