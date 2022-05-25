from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from ..models import ReservedShoe, Shoe, Cart
home_view = Blueprint('home_view', __name__)
from .. import db

@home_view.route('/')
@home_view.route('/home')
def home_page():
    recently_added = Shoe.query.order_by(Shoe.id.desc()).limit(5)

    shoes = Shoe.query.all()
    brands = []
    for shoe in shoes:
        if not brands.__contains__(shoe.brand):
            brands.append(shoe.brand)
    brands.sort()
    
    return render_template("index.html", current_user=current_user, recently_added=recently_added, brands=brands)
