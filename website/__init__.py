from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'sneakerhead.db'

def create_app():
    app = Flask(__name__)
    
    # db setup
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    # load blueprints
    from .views.inventory import inventory_view
    app.register_blueprint(inventory_view, url_prefix='/')
    return app