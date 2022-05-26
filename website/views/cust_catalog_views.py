from flask import Blueprint, render_template, request
from flask_login import current_user
from ..models import Shoe


PER_PAGE = 36
cust_catalog_views = Blueprint('cust_catalog_views', __name__)


@cust_catalog_views.route('/releases', methods=['GET'])
def releases_page():
    title = "New Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.releases_page'

    return render_template('customer/catalog.html', 
    current_user=current_user, 
    title=title, 
    collection=collection, 
    routeUrl=routeUrl)


@cust_catalog_views.route('/mens/releases', methods=['GET'])
def mens_releases_page():
    title = "New Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.filter_by(audience="Men").paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.mens_releases_page'

    return render_template('customer/catalog.html', 
    title=title, 
    collection=collection, 
    routeUrl=routeUrl)


@cust_catalog_views.route('/womens/releases', methods=['GET'])
def womens_releases_page():
    title = "New Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.filter_by(audience="Women").paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.womens_releases_page'

    return render_template('customer/catalog.html', 
    title=title, 
    current_user=current_user, 
    collection=collection, 
    routeUrl=routeUrl)


@cust_catalog_views.route('/kids/releases', methods=['GET'])
def kids_releases_page():
    title = "New Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.filter_by(audience="Children").paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.kids_releases_page'

    return render_template('customer/catalog.html', 
    title=title, 
    current_user=current_user, 
    collection=collection, 
    routeUrl=routeUrl)


@cust_catalog_views.route('/<string:brand>/releases', methods=['GET'])
def brand_releases_page(brand):
    title = brand + " New Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.filter(Shoe.brand.like('%'+brand+'%')).paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.brand_releases_page'

    return render_template('customer/catalog.html', 
    title=title, 
    current_user=current_user, 
    collection=collection, 
    routeUrl=routeUrl,
    brand=brand)


@cust_catalog_views.route('/releases/browse/<string:searchQuery>')
def search_any_product(searchQuery):
    title = "Sneaker Headz Releases"
    page = request.args.get('page', 1, type=int)
    collection = Shoe.query.filter(Shoe.name.like('%'+searchQuery+'%') | Shoe.brand.like('%'+searchQuery+'%')).paginate(page=page, per_page=PER_PAGE)
    routeUrl = 'cust_catalog_views.search_any_product'

    return render_template('customer/catalog.html', 
    title=title, 
    collection=collection, 
    routeUrl=routeUrl,
    searchQuery=searchQuery)


@cust_catalog_views.route('/product/<int:id>', methods=['GET'])
def display_product(id):
    shoe = Shoe.query.get_or_404(id)
    return render_template('customer/product.html', 
    current_user=current_user, 
    shoe=shoe)
    