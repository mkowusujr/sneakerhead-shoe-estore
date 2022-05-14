from flask import Blueprint, render_template

inventory_view = Blueprint('inventory_view', __name__)

@inventory_view.route('/inventory')
def inventory():
    return "Hello Inventory"