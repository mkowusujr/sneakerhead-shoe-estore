from flask import Blueprint, Response, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from ..models import Color, Quantity_Per_Size, Shoe
admin_catalog_views = Blueprint('admin_catalog_views', __name__)
from .. import db

@admin_catalog_views.before_request
@login_required
def admin_only():
    pass

"""
POST METHODS
""" 
@admin_catalog_views.route('/inventory', methods=['POST'])
def add_to_inventory():
    new_shoe = Shoe(
        name = request.form['name'],
        brand = request.form['brand'],
        audience = request.form['audience'],
        price = request.form['price']
    )

    db.session.add(new_shoe)
    db.session.commit()

    return redirect(url_for('admin_catalog_views.display_inventory'))

@admin_catalog_views.route('/inventory/<int:shoe_id>', methods=['POST'])
def add_product_color(shoe_id):
    color = Color(
        color = request.form['color']
    )
    db.session.add(color)
    db.session.commit()

    shoe = Shoe.query.get_or_404(shoe_id)
    shoe.colors.append(color)
    db.session.add(shoe)
    db.session.commit()

    return redirect(url_for('admin_catalog_views.display_shoe', id=shoe_id))


@admin_catalog_views.route('/inventory/<int:shoe_id>/<int:color_id>', methods=['POST'])
def add_product_color_quantity(shoe_id, color_id):
    quan = Quantity_Per_Size(
        size = request.form['size'],
        quantity = request.form['quantity']
    )
    db.session.add(quan)
    db.session.commit()

    color = Color.query.get_or_404(color_id)
    color.quan_per_size.append(quan)
    db.session.add(color)
    db.session.commit()
    return redirect(url_for('admin_catalog_views.display_shoe', id=shoe_id))


"""
GET METHODS
"""
@admin_catalog_views.route('/inventory', methods=['GET'])
def display_inventory():
    inventory = Shoe.query.all()
    return render_template('admin/catalog.html', current_user=current_user, inventory=inventory)
  

@admin_catalog_views.route('/inventory/<int:id>', methods=['GET'])
def display_shoe(id):
    shoe = Shoe.query.get_or_404(id)
    return render_template('admin/product.html', current_user=current_user, shoe=shoe)


"""
UPDATE METHODS
"""
@admin_catalog_views.route('/inventory/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    updated_shoe = Shoe.query.get_or_404(id)
    updated_shoe.name = data['name']
    updated_shoe.brand = data['brand']
    updated_shoe.audience = data['audience']
    updated_shoe.price = data['price']
    db.session.commit()
    return Response(url_for('admin_catalog_views.display_inventory'), 200)


@admin_catalog_views.route('/inventory/<int:shoe_id>/<int:color_id>', methods=['PUT'])
def update_product_color(shoe_id, color_id):
    data = request.get_json()
    color = Color.query.get_or_404(color_id)
    color.color = data['color']
    db.session.add(color)
    db.session.commit()
    print(data)
    return Response(url_for('admin_catalog_views.display_shoe', id=shoe_id), 200)


@admin_catalog_views.route('/inventory/<int:shoe_id>/<int:color_id>/<int:quan_id>', methods=['PUT'])
def update_product_color_quantity(shoe_id, color_id, quan_id):
    data = request.get_json()
    quan = Quantity_Per_Size.query.get_or_404(quan_id)
    quan.quantity = data['quantity']
    db.session.add(quan)
    db.session.commit()
    print(data)
    return Response(url_for('admin_catalog_views.display_shoe', id=shoe_id), 200)


"""
DELETE METHODS
"""
@admin_catalog_views.route('/inventory/<int:id>', methods=['Delete'])
def delete_from_inventory(id):
    shoe = Shoe.query.get_or_404(id)
    db.session.delete(shoe)
    db.session.commit()
    return Response(url_for('admin_catalog_views.display_inventory'), 200)


@admin_catalog_views.route('/inventory/<int:shoe_id>/<int:color_id>', methods=['DELETE'])
def delete_product_color(shoe_id, color_id):
    color = Color.query.get_or_404(color_id)
    db.session.delete(color)
    db.session.commit()
    return Response(url_for('admin_catalog_views.display_shoe', id=shoe_id), 200)

@admin_catalog_views.route('/inventory/<int:shoe_id>/<int:color_id>/<int:quan_id>', methods=['DELETE'])
def delete_product_color_quantity(shoe_id, color_id, quan_id):
    quan = Quantity_Per_Size.query.get_or_404(quan_id)
    db.session.delete(quan)
    db.session.commit()
    return Response(url_for('admin_catalog_views.display_shoe', id=shoe_id), 200)
