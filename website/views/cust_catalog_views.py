from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
cust_catalog_views = Blueprint('cust_catalog_views', __name__)
from .. import db

@cust_catalog_views.route('/releases')
def releases_page():
    return "<h1>Welcome to our Releases</h1>"