from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
inventory_view = Blueprint('inventory_view', __name__)
from .. import db

@inventory_view.route('/inventory')
def inventory():
    return "Hello World"
