from flask import Blueprint, render_template
from flask_login import current_user
from ..models import Shoe
cust_catalog_views = Blueprint('cust_catalog_views', __name__)


@cust_catalog_views.route('/releases', methods=['GET'])
def releases_page():
    title = "New Releases"
    collection = Shoe.query.all()
    return render_template('cust_catalog/catalog.html', current_user=current_user, title=title, collection=collection)


@cust_catalog_views.route('/mens/releases', methods=['GET'])
def mens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Men")
    return render_template('cust_catalog/catalog.html', title=title, collection=collection)


@cust_catalog_views.route('/womens/releases', methods=['GET'])
def womens_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Women")
    return render_template('cust_catalog/catalog.html', title=title, current_user=current_user, collection=collection)


@cust_catalog_views.route('/kids/releases', methods=['GET'])
def kids_releases_page():
    title = "New Releases"
    collection = Shoe.query.filter_by(audience="Children")
    return render_template('cust_catalog/catalog.html', title=title, current_user=current_user, collection=collection)


@cust_catalog_views.route('/<string:brand>/releases', methods=['GET'])
def brand_releases_page(brand):
    title = brand + " New Releases"
    collection = Shoe.query.filter_by(brand=brand)
    return render_template('cust_catalog/catalog.html', title=title, current_user=current_user, collection=collection)


@cust_catalog_views.route('/releases/browse/<string:searchQuery>')
def search_any_product(searchQuery):
    title = "Sneaker Headz Releases"
    collection = []

    similar_names = Shoe.query.filter(Shoe.name.like('%'+searchQuery+'%')).all()
    similar_brands = Shoe.query.filter(Shoe.brand.like('%'+searchQuery+'%')).all()
    collection.extend(similar_names)
    collection.extend(similar_brands)
    
    return render_template('cust_catalog/catalog.html', title=title, collection=collection)


@cust_catalog_views.route('/product/<int:id>', methods=['GET'])
def display_product(id):
    shoe = Shoe.query.get_or_404(id)
    return render_template('cust_catalog/product.html', current_user=current_user, shoe=shoe)
    