from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
from .models import Customer, Cart, ReservedShoe, Shoe
from .views.acct_mgmt_views import acct_mgmt_views
from .views.admin_catalog_view import admin_catalog_view
from .views.cust_cart_views import cust_cart_view
from .views.cust_catalog_views import cust_catalog_views
from .views.home_view import home_view

DB_NAME = 'sneakerhead.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "yeet"
    # db setup
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    create_database(app)

    # load blueprints
    app.register_blueprint(acct_mgmt_views, url_prefix='/')
    app.register_blueprint(admin_catalog_view, url_prefix='/')
    app.register_blueprint(cust_cart_view, url_prefix='/')
    app.register_blueprint(cust_catalog_views, url_prefix='/')
    app.register_blueprint(home_view, url_prefix='/')
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
