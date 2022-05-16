from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
home_view = Blueprint('home_view', __name__)
from .. import db

@home_view.route('/')
@home_view.route('/home')
def home_page():
    return render_template("home.html")