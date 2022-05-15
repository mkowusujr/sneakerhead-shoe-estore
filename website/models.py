from flask_sqlalchemy import SQLAlchemy

from . import db
# from flask_login import UserMixin

class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)


class Cart(db.Model):
    id = db.Column(db.Integer(), primary_key=True)


class ReservedShoe(db.Model):
    __tablename__ = 'reserved_shoe'
    id = db.Column(db.Integer(), primary_key=True)
    shoe_id = db.Column(db.Integer(), db.ForeignKey('shoe.id')) # one to one
    reserved_shoe = db.relationship("Shoe", backref="reserved_shoe", uselist=False)
    quantity = db.Column(db.Integer(), nullable=False)


class Shoe(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    brand = db.Column(db.String(length=30), nullable=False)
    color = db.Column(db.String(length=30), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(), nullable=False)