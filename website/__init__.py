from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# from . import models

db = SQLAlchemy()
from .models import Customer, Cart, ReservedShoe, Shoe
from .views.inventory import inventory_view

DB_NAME = 'sneakerhead.db'

def create_app():
    app = Flask(__name__)
    
    # db setup
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    create_database(app)

    # load blueprints
    app.register_blueprint(inventory_view, url_prefix='/')
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)