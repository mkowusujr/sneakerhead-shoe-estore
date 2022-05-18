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
    # data1 = request.get_data()
    data = request.get_json()
    updated_shoe = Shoe.query.get_or_404(id)
    updated_shoe.name = data['name']
    updated_shoe.brand = data['brand']
    updated_shoe.price = data['price']
    db.session.commit()
    x = Shoe.from_json(data)
    # x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    
    # shoe = Shoe(
    #     id = id,
    #     name = data['name'],
    #     brand = data['brand'],
    #     color = "N/A",
    #     size = 100,
    #     quantity = 100,
    #     price = data['price']
    # )
    # data3 = request.json()
    # data4 = json.loads(request.data)
    return Response("", 200)


@admin_catalog_view.route('/inventory/<int:id>', methods=['Delete'])
def remove_from_inventory(id):
    shoe = Shoe.query.filter_by(id=id).first_or_404()
    db.session.delete(shoe)
    db.session.commit()
    return Response("", 200)