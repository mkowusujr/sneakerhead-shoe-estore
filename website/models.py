from flask_sqlalchemy import SQLAlchemy
import json
from . import db
# from flask_login import UserMixin


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer(), primary_key=True)
    # displayname = db.Column()
    # email = db.Column()
    # cartid = db.Column()


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer(), primary_key=True)

    # one to many relationship, one cart with many shoes
    shoes = db.relationship("ReservedShoe", back_populates="cart", lazy=True)

    def __repr__(self):
        return '<Cart {},shoes={}>'.format(self.id, self.shoes)


class ReservedShoe(db.Model):
    __tablename__ = 'reserved_shoe'

    id = db.Column(db.Integer(), primary_key=True)

    # one to one relationship, one reserved shoe 'collection' inside one cart
    cartid = db.Column(db.Integer(), db.ForeignKey('cart.id'))
    # allows you to access the entire cart that is linked to this reserved shoe
    cart = db.relationship('Cart', back_populates='shoes')

    # one to one relationship, one reserved shoe in a user's cart to one shoe in the inventory
    shoe_id = db.Column(db.Integer(), db.ForeignKey('shoe.id'))
    # allows you to access the entire shoe from this reserved shoe
    reserved_shoe = db.relationship(
        "Shoe", backref="reserved_shoe", uselist=False)

    # number of this shoe in the cart
    quantity = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return """<ReservedShoe {}, cartid={}, 
        cart={}, shoeid={}, reserved_shoe={}, quan={}>""".format(self.id, self.cartid, self.cart,
                                                                        self.shoe_id, self.reserved_shoe, self.quantity)


class Shoe(db.Model):
    __tablename__ = 'shoe'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    brand = db.Column(db.String(length=30), nullable=False)
    audience = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    # one to many relationship, one shoe many colors
    # if a color is deleted all its children are too, if one of its
    #children is delete it will be gone from color's list of children
    colors = db.relationship("Color", back_populates="shoe", lazy=True, cascade='all, delete, delete-orphan') 
    
    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)

    def __repr__(self):
        return '<Shoe {}, name={}>'.format(self.id, self.name)


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer(), primary_key=True)
    color = db.Column(db.String(length=30))
    
    # one to many relationship, one color many quantity per sizes
    quan_per_size = db.relationship("Quantity_Per_Size", back_populates="color", lazy=True, cascade='all, delete, delete-orphan')
    
    # Many colors belonging to one shoe
    shoe_id = db.Column(db.Integer(), db.ForeignKey('shoe.id'))
    shoe = db.relationship('Shoe', back_populates='colors')

    def __repr__(self):
        return '<clrszquan {}, quantbl={}, {}>'.format(self.id, self.quantity_table_id, self.quantity_table)


class Quantity_Per_Size(db.Model):
    __tablename__ = 'quantity_per_size'

    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Float())
    quantity = db.Column(db.Integer())

    # many quantity per sizes belonging to one color
    color_id = db.Column(db.Integer(), db.ForeignKey('color.id'))
    color = db.relationship('Color', back_populates='quan_per_size')
    def __repr__(self):
        return "<quanpersize {}, size {}, quan{}>".format(self.id, self.size, self.quantity)