from select import select
from flask import Blueprint, Response, render_template, redirect, request, json, jsonify
from ..models import Color, Quantity_Per_Size, ReservedShoe, Shoe, Cart
admin_catalog_view = Blueprint('admin_catalog_view', __name__)
from .. import db
from types import SimpleNamespace
  
@admin_catalog_view.route('/inventory', methods=['POST'])
def add_to_inventory():
    new_shoe = Shoe(
        name = request.form['name'],
        brand = request.form['brand'],
        # color = request.form['color'],
        # size = request.form['size'],
        # quantity = request.form['quantity'],
        price = request.form['price']
    )

    db.session.add(new_shoe)
    db.session.commit()

    return redirect('/inventory')


@admin_catalog_view.route('/inventory', methods=['GET'])
def display_inventory():
    inventory = Shoe.query.all()
    return render_template('admin_catalog.html', inventory=inventory)
  
@admin_catalog_view.route('/inventory/<int:id>')
def display_shoe(id):
    shoe = Shoe.query.get_or_404(id)
    return render_template('admin_catalog_product.html', shoe=shoe)

@admin_catalog_view.route('/inventory/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    updated_shoe = Shoe.query.get_or_404(id)
    updated_shoe.name = data['name']
    updated_shoe.brand = data['brand']
    updated_shoe.price = data['price']
    db.session.commit()
    return Response("/inventory", 200)

@admin_catalog_view.route('/inventory/<int:shoe_id>/<int:color_id>', methods=['PUT'])
def update_product_color(shoe_id, color_id):
    data = request.get_json()
    color = Color.query.get_or_404(color_id)
    color.color = data['color']
    db.session.add(color)
    db.session.commit()
    print(data)
    return Response("/inventory/" + str(shoe_id), 200)


@admin_catalog_view.route('/inventory/<int:shoe_id>/<int:color_id>/<int:quan_id>', methods=['PUT'])
def update_product_color_quantity(shoe_id, color_id, quan_id):
    data = request.get_json()
    quan = Quantity_Per_Size.query.get_or_404(quan_id)
    quan.quantity = data['quantity']
    db.session.add(quan)
    db.session.commit()
    print(data)
    return Response("/inventory/" + str(shoe_id), 200)

@admin_catalog_view.route('/inventory/<int:id>', methods=['Delete'])
def remove_from_inventory(id):
    shoe = Shoe.query.get_or_404(id)
    db.session.delete(shoe)
    db.session.commit()
    return Response("/inventory", 200)

@admin_catalog_view.route('/inventory/<int:shoe_id>/<int:color_id>/<int:quan_id>', methods=['DELETE'])
def delete_product_color_quantity(shoe_id, color_id, quan_id):
    quan = Quantity_Per_Size.query.get_or_404(quan_id)
    db.session.delete(quan)
    db.session.commit()
    return Response("/inventory/" + str(shoe_id), 200)
