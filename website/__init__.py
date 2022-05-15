from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from . import models

from .views.inventory import inventory_view

db = SQLAlchemy()
DB_NAME = 'sneakerhead.db'

def create_app():
    app = Flask(__name__)
    
    # db setup
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .models import Customer, Cart, ReservedShoe, Shoe
    create_database(app)

    # load blueprints
    app.register_blueprint(inventory_view, url_prefix='/')
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)