from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from ..models import ReservedShoe, Shoe, Cart
cust_cart_views = Blueprint('cust_cart_views', __name__)
from .. import db


@cust_cart_views.before_request
@login_required
def login_to_access():
    pass


@cust_cart_views.route('/cart', methods=['GET'])
def display_cart_page():
    cart = current_user.cart.shoes
    return render_template('cart.html', current_user=current_user, cart=cart)


@cust_cart_views.route('/cart', methods=['POST'])
def add_to_cart():
    id = int(request.get_json())
    shoe = Shoe.query.get_or_404(id)

    shoe_is_in_cart = False
    for shoe_in_cart in current_user.cart.shoes:
        if shoe_in_cart.shoe_id == shoe.id:
            shoe_is_in_cart = True
            shoe_in_cart.quantity += 1

    if not shoe_is_in_cart:
        added_shoe = ReservedShoe(
            quantity = 1
        )
        added_shoe.reserved_shoe = shoe
        db.session.add(added_shoe)
        current_user.cart.shoes.append(added_shoe)
        db.session.add(current_user)

        db.session.commit()

    return redirect(url_for('cust_cart_views.display_cart_page'))