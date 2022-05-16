from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
admin_catalog_view = Blueprint('admin_catalog_view', __name__)
from .. import db

@admin_catalog_view.route('/inventory')
def inventory_page():
    return "<h1>Welcome to the Inventory</h1>"