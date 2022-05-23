from select import select
from flask import Blueprint, render_template, redirect
from flask_login import login_required
from ..models import ReservedShoe, Shoe, Cart
cust_cart_view = Blueprint('cust_cart_view', __name__)
from .. import db

@cust_cart_view.route('/cart')
@login_required
def cart_page():
    return "<h1>Welcome to your Cart</h1>"