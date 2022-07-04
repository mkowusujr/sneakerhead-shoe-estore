"""
Sets up the entire project 

Author: Mathew Owusu
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()

# Import all the views
from .models import Customer, Cart, ReservedShoe, Shoe
from .views.acct_mgmt_views import acct_mgmt_views
from .views.admin_catalog_views import admin_catalog_views
from .views.cust_cart_views import cust_cart_views
from .views.cust_catalog_views import cust_catalog_views
from .views.home_view import home_view
from .views.transcations_views import transcations_views
from . import init_shoe_data

# Name of the database file
DB_NAME = 'sneakerhead.db'


def create_app():
    """
    Creates a new Flask app and connects to the shoe store databse.
    It also sets up the login manager for keeping track of user authentication.

    Returns:
        Flask App: A Flask Web app with database and login manger
        set up
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "not_password"

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
    app.register_blueprint(transcations_views, url_prefix='/')
    
    # populate_db_with_shoes()
    return app


def create_database(app):
    """
    Creates the database of the web application if the database file
    doesn't exist.
    If it has to create a new databse file, it will populate it with 
    the shoe data

    Parameters:
        app (Flask App): The Flask web app
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        init_shoe_data.populate_db_with_shoes()
  