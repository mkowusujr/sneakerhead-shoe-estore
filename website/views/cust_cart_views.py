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
    id = int(request.form['shoe_id'])
    quantity = int(request.form['quantity'])

    user_cart = current_user.cart
    shoe_in_cart = ReservedShoe.query.filter_by(cartid=user_cart.id, shoe_id=id).first()

    if shoe_in_cart:
        shoe_in_cart.quantity += quantity
        db.session.commit()
    else:
        added_shoe = ReservedShoe(
            quantity = quantity
        )
        added_shoe.reserved_shoe = Shoe.query.get_or_404(id)
        db.session.add(added_shoe)
        current_user.cart.shoes.append(added_shoe)
        db.session.add(current_user)

        db.session.commit()

    return redirect(url_for('cust_cart_views.display_cart_page'))

@cust_cart_views.route('/cart/<int:id>', methods=['POST'])
def quick_add():
    shoe = ReservedShoe.query.get_or_404(id)
    shoe.quantity += 1
    return redirect(url_for('cust_cart_views.display_cart_page'))