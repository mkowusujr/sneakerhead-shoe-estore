from flask import Blueprint, render_template, redirect
from flask_login import current_user
from ..models import ReservedShoe, Shoe, Cart
cust_catalog_views = Blueprint('cust_catalog_views', __name__)
from .. import db

@cust_catalog_views.route('/releases', methods=['GET'])
def releases_page():
    title = "New Releases"
    collection = Shoe.query.all()
    return render_template('catalog.html', current_user=current_user, title=title, collection=collection)

@cust_catalog_views.route('/mens/releases', methods=['GET'])
def mens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Men")
    return render_template('catalog.html', title=title, collection=collection)

@cust_catalog_views.route('/womens/releases', methods=['GET'])
def womens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Womens")
    return render_template('catalog.html', title=title, current_user=current_user, collection=collection)

@cust_catalog_views.route('/kids/releases', methods=['GET'])
def kids_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Kids")
    return render_template('catalog.html', title=title, current_user=current_user, collection=collection)

@cust_catalog_views.route('/<string:brand>/releases', methods=['GET'])
def brand_releases_page(brand):
    title = brand + " New Releases"
    collection = Shoe.query.filter_by(brand=brand)
    return render_template('catalog.html', title=title, current_user=current_user, collection=collection)

@cust_catalog_views.route('/releases/browse/<string:searchQuery>')
def search_any_product(searchQuery):
    title = "Sneaker Headz Releases"
    collection = []
    similar_names = Shoe.query.filter(Shoe.name.like('%'+searchQuery+'%')).all()
    similar_brands = Shoe.query.filter(Shoe.brand.like('%'+searchQuery+'%')).all()
    collection.extend(similar_names)
    collection.extend(similar_brands)
    # collection.ppend()
    return render_template('catalog.html', title=title, collection=collection)