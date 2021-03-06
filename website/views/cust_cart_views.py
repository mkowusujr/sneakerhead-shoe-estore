"""
Manages all routes related to the current user's cart

Author: Mathew Owusu Jr
"""


from flask import Blueprint, Response, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from ..models import Quantity_Per_Size, ReservedShoe, Shoe, Color
cust_cart_views = Blueprint('cust_cart_views', __name__)
from .. import db


@cust_cart_views.before_request
@login_required
def login_to_access():
    """
    Acts as a middle ware that ensure none of this blueprints routes can be
    accessed if no user is currently logged in
    """
    pass


@cust_cart_views.route('/cart', methods=['GET'])
def display_cart_page():
    """
    Display the user's cart

    Returns:
        A rendered HTML template
    """
    cart = current_user.cart.shoes
    total_price = 0
    for shoe in cart:
        total_price += (shoe.quantity * shoe.reserved_shoe.price)
        
    return render_template('acct_mgmt/cart.html', 
    current_user=current_user, 
    cart=cart, 
    total_price=total_price)


@cust_cart_views.route('/cart', methods=['POST'])
def add_to_cart():
    """
    Adds a shoe to the user's cart

    Returns:
        Redirects the page to cart page again
    """
    id = int(request.form['shoe_id'])
    quantity = int(request.form['quantity'])
    color = (request.form['color'])
    size = float(request.form['size'])

    user_cart = current_user.cart
    shoe_in_cart = ReservedShoe.query.filter_by(
        cart_id=user_cart.id, 
        shoe_id=id,
        color=color,
        size=size).first()

    if shoe_in_cart:
        color = Color.query.filter_by(shoe_id=shoe_in_cart.shoe_id).first()
        max_quantity = Quantity_Per_Size.query.filter_by(color_id=color.id, size=shoe_in_cart.size).first()
        if max_quantity.quantity >= (shoe_in_cart.quantity + quantity):
            shoe_in_cart.quantity += quantity
            db.session.commit()
        # else you exceeded the max quantity
        else:
            return ('', 204)
    else:
        added_shoe = ReservedShoe(
            quantity = quantity,
            color=request.form['color'],
            size=request.form['size']
        )
        added_shoe.reserved_shoe = Shoe.query.get_or_404(id)
        db.session.add(added_shoe)
        current_user.cart.shoes.append(added_shoe)
        db.session.add(current_user)

        db.session.commit()

    return redirect(url_for('cust_cart_views.display_cart_page'))


@cust_cart_views.route('/cart/<int:id>', methods=['POST'])
def quick_add(id):
    """
    Adds to the quantity of a shoe in the user's cart

    Parameters:
        id (int): The id of the cart item

    Returns:_description_
        HTTP Reponse: Send the url for the display cart page and a http status
        of 200 for success
    """
    shoe = ReservedShoe.query.get_or_404(id)
    color = Color.query.filter_by(shoe_id=shoe.shoe_id).first()
    max_quantity = Quantity_Per_Size.query.filter_by(color_id=color.id, size=shoe.size).first()
    if max_quantity.quantity >= (shoe.quantity + 1):
        shoe.quantity += 1
    db.session.commit()
    return Response(url_for('cust_cart_views.display_cart_page'), 200)


@cust_cart_views.route('/cart/<int:id>', methods=['DELETE'])
def quick_remove(id):
    """
    Removes from the quantity of a shoe in the user's cart

    Parameters:
        id (int): The id of the cart item

    Returns:_description_
        HTTP Reponse: Send the url for the display cart page and a http status
        of 200 for success
    """
    shoe = ReservedShoe.query.get_or_404(id)
    shoe.quantity -= 1
    if shoe.quantity == 0:
        db.session.delete(shoe)
    db.session.commit()
    return Response(url_for('cust_cart_views.display_cart_page'), 200)


@cust_cart_views.route('/cart/remove/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    """
    Removes a shoe from the user's cart

    Parameters:
        id (int): The id of the cart item

    Returns:
        HTTP Reponse: Send the url for the display cart page and a http status
        of 200 for success
    """
    shoe = ReservedShoe.query.get_or_404(id)
    db.session.delete(shoe)
    db.session.commit()
    return Response(url_for('cust_cart_views.display_cart_page'), 200)