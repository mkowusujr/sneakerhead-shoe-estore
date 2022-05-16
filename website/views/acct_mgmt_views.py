from select import select
from flask import Blueprint, render_template, redirect
from ..models import ReservedShoe, Shoe, Cart
acct_mgmt_views = Blueprint('acct_mgmt_views', __name__)
from .. import db

@acct_mgmt_views.route('/accounts')
def placeholder():
    return "<h1>Welcome to your Account page</h1>"