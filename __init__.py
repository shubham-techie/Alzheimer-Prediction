from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init DB
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='SECRET-KEY';
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth routes
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



