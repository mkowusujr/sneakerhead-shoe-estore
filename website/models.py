from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin

class Customer(db.Model, UserMixin):
    pass


class Cart(db.Model):
    pass


class ReservedShoes(db.Model):
    pass


class Shoes(db.Model):
    pass