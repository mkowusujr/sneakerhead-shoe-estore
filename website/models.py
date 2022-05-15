from flask_sqlalchemy import SQLAlchemy

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
    # custid = db.Column(db.Integer(), db.ForeignKey('customer.id')) # one to one
    
    # shoe_id = db.Column(db.Integer(), db.ForeignKey('shoe.id')) # one to many
    shoes = db.relationship("ReservedShoe", back_populates="cart", lazy=True)
    def __repr__(self):
        return '<Cart {},shoes={}'.format(self.id, self.shoes)

class ReservedShoe(db.Model):
    __tablename__ = 'reserved_shoe'
    id = db.Column(db.Integer(), primary_key=True)
    cartid = db.Column(db.Integer(), db.ForeignKey('cart.id'))
    cart = db.relationship('Cart', back_populates='shoes')

    shoe_id = db.Column(db.Integer(), db.ForeignKey('shoe.id')) # one to one
    reserved_shoe = db.relationship("Shoe", backref="reserved_shoe", uselist=False)
    quantity = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return '<ReservedShoe {}, cartid={}, shoeid={}, quan={}'.format(self.id, self.cartid,
        self.shoe_id, self.quantity)
    


class Shoe(db.Model):
    __tablename__ = 'shoe'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    brand = db.Column(db.String(length=30), nullable=False)
    color = db.Column(db.String(length=30), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    def __repr__(self):
        return '<Shoe {}, name={}'.format(self.id, self.name)
