from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
inventory_view = Blueprint('inventory_view', __name__)
from .. import db

@inventory_view.route('/inventory')
def inventory():
    new_shoe = Shoe(
        name="Yeezy Boost 700",
        brand="Yeezy",
        color="Black",
        size=9.5,
        quantity=100,
        price=250.00
    )
    db.session.add(new_shoe)
    db.session.commit()

    # new_cart = Cart()
    # db.session.add(new_cart)
    # db.session.commit()

    new_cart = db.session.query(Cart).first()
    new_shoe = Shoe.query.filter_by(id=2).first()
    reserved_shoe = ReservedShoe(
        cartid=new_cart.id,
        shoe_id=new_shoe.id,
        quantity=1
    )
    db.session.add(reserved_shoe)
    db.session.commit()

    new_cart.shoes.append(reserved_shoe)
    db.session.add(new_cart)
    db.session.commit()
    print(db.session.query(Cart).first())
    print_cart = db.session.query(Cart).first()
    return print_cart.__repr__()
