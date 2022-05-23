from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()

from .models import Customer, Cart, ReservedShoe, Shoe
from .views.acct_mgmt_views import acct_mgmt_views
from .views.admin_catalog_views import admin_catalog_views
from .views.cust_cart_views import cust_cart_views
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

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'acct_mgmt_views.display_login_page'
    login_manager.init_app(app)
    @login_manager.user_loader 
    def load_user(id):
        return Customer.query.get(int(id))

    # load blueprints
    app.register_blueprint(acct_mgmt_views, url_prefix='/')
    app.register_blueprint(admin_catalog_views, url_prefix='/')
    app.register_blueprint(cust_cart_views, url_prefix='/')
    app.register_blueprint(cust_catalog_views, url_prefix='/')
    app.register_blueprint(home_view, url_prefix='/')
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)

