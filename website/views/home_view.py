from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
home_view = Blueprint('home_view', __name__)
from .. import db

@home_view.route('/')
@home_view.route('/home')
def home_page():
    
    recently_added = Shoe.query.order_by(Shoe.id.desc()).limit(5)
    return render_template("home.html", recently_added=recently_added)

@home_view.route('/test')
def test():
    hack_redirect = """
    <script>
        window.location.href = "/inventory"
    </script>
    """
    return hack_redirect