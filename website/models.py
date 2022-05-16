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
    color = db.Column(db.String(length=30), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Shoe {}, name={}>'.format(self.id, self.name)
