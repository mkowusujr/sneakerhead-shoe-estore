"""
Manages all routes related to home

Author: Mathew Owusu Jr
"""

from flask import Blueprint, render_template
from flask_login import current_user
from ..models import Shoe
home_view = Blueprint('home_view', __name__)

@home_view.route('/')
@home_view.route('/home')
def home_page():
    """
    Fetches recently added shoes to the database and displays it on the home page

    Returns:
        A rendered HTML template
    """
    recently_added = Shoe.query.filter_by(audience='Men').order_by(Shoe.id.desc()).limit(5)
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
    
    return render_template("index.html", 
    current_user=current_user, 
    recently_added=recently_added, 
    brands=brands)
