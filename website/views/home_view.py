from flask import Blueprint, render_template
from flask_login import current_user
from ..models import Shoe
home_view = Blueprint('home_view', __name__)

@home_view.route('/')
@home_view.route('/home')
def home_page():
    recently_added = Shoe.query.order_by(Shoe.id.desc()).limit(5)
    brands = [
        "adidas",
        "aldo",
        "converse",
        "fila",
        "lacoste",
        "new balance",
        "nike",
        "Polo Ralph Lauren",
        "puma",
        "reebook",
        "sketchers",
        "steve madden",
        "timberland",
        "hilfiger",
        "under armour",
        "vans"
        ]
    # shoes = Shoe.query.all()
    # brands = []
    # for shoe in shoes:
    #     if not brands.__contains__(shoe.brand):
    #         brands.append(shoe.brand)
    # brands.sort()
    
    return render_template("index.html", 
    current_user=current_user, 
    recently_added=recently_added, 
    brands=brands)
