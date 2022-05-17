from select import select
from flask import Blueprint, Response, render_template, redirect, request
from ..models import ReservedShoe, Shoe, Cart
admin_catalog_view = Blueprint('admin_catalog_view', __name__)
from .. import db

@admin_catalog_view.route('/inventory', methods=['GET'])
def display_inventory():
    inventory = Shoe.query.all()
    return render_template('admin_catalog.html', inventory=inventory)
    

@admin_catalog_view.route('/inventory', methods=['POST'])
def add_to_inventory():
    new_shoe = Shoe(
        name = request.form['name'],
        brand = request.form['brand'],
        color = request.form['color'],
        size = request.form['size'],
        quantity = request.form['quantity'],
        price = request.form['price']
    )

    db.session.add(new_shoe)
    db.session.commit()

    return redirect('/inventory')


@admin_catalog_view.route('/inventory/<int:id>', methods=['Delete'])
def remove_from_inventory(id):
    shoe = Shoe.query.filter_by(id=id).first_or_404()
    db.session.delete(shoe)
    db.session.commit()
    return Response("", 200)