from flask import Blueprint, Response, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from ..models import Color, Customer, Quantity_Per_Size, Transcation, PurchasedShoe, Shoe
transcations_views = Blueprint('transcations_views', __name__)
from .. import db

@transcations_views.before_request
@login_required
def login_to_access():
    pass


@transcations_views.route('/user/transcations', methods=['GET'])
def display_transcations():
    user = Customer.query.get_or_404(current_user.id)
    transcations = user.transcations
    return render_template('customer/transcations.html', 
    current_user=current_user, 
    transcations=transcations)


@transcations_views.route('/user/transcations', methods=['POST'])
def add_transcation():
    user = Customer.query.get_or_404(current_user.id)
    
    new_transc = Transcation(
        owner = user,
        owner_id = user.id,
        total_price = 0
    )
    db.session.add(new_transc)
    db.session.commit()

    cart = current_user.cart
    for shoe in cart.shoes:
        purchased_shoe = PurchasedShoe (
            name = shoe.reserved_shoe.name,
            color = shoe.color,
            size = shoe.size,
            quantity = shoe.quantity,
            price = shoe.reserved_shoe.price,
            shoe_id = shoe.reserved_shoe.id,
            transc = new_transc,
            transc_id = new_transc.id
        )
        inventory_shoe = Shoe.query.get_or_404(shoe.reserved_shoe.id)
        inventory_shoe_color = Color.query.filter_by(color=shoe.color, shoe_id=inventory_shoe.id).first()
        inventory_quantity = Quantity_Per_Size.query.get_or_404(inventory_shoe_color.id)

        inventory_quantity.quantity -= shoe.quantity
        db.session.add(inventory_shoe)
        db.session.add(purchased_shoe)
        db.session.delete(shoe)
        db.session.commit()

        new_transc.shoes.append(purchased_shoe)
        new_transc.total_price += (shoe.quantity * shoe.reserved_shoe.price)
        db.session.add(new_transc)
        db.session.commit()

    user.transcations.append(new_transc)    
    db.session.add(user)
    db.session.commit()


    return redirect(url_for('transcations_views.display_transcations'))