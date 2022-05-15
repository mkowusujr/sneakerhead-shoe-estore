from flask import Blueprint, render_template, redirect
from ..models import Shoe
inventory_view = Blueprint('inventory_view', __name__)
from .. import db

@inventory_view.route('/inventory')
def inventory():
    new_shoe = Shoe(
        name="Yeezy Boost 350",
        brand="Yeezy",
        color="Zebra",
        size=9.5,
        quantity=100,
        price=250.00
    )
    db.session.add(new_shoe)
    db.session.commit()
    return "Hello Inventory"