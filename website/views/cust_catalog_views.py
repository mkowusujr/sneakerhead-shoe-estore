from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
cust_catalog_views = Blueprint('cust_catalog_views', __name__)
from .. import db

@cust_catalog_views.route('/releases')
def releases_page():
    title = "New Releases"
    collection = Shoe.query.all()
    return render_template('catalog.html', title=title, collection=collection)

@cust_catalog_views.route('/mens/releases')
def mens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Men")
    return render_template('catalog.html', title=title, collection=collection)

@cust_catalog_views.route('/womens/releases')
def womens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Womens")
    return render_template('catalog.html', title=title, collection=collection)

@cust_catalog_views.route('/kids/releases')
def kids_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Kids")
    return render_template('catalog.html', title=title, collection=collection)