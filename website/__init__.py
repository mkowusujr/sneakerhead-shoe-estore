from flask import Flask

def create_app():
    app = Flask(__name__)

    # load blueprints
    from .views.inventory import inventory_view
    app.register_blueprint(inventory_view, url_prefix='/')
    return app