from flask import Blueprint, render_template, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Customer
from .. import db

acct_mgmt_views = Blueprint('acct_mgmt_views', __name__)

@acct_mgmt_views.route('/signup', methods=["GET"])
def display_signup_page():
    return render_template('signup.html')

@acct_mgmt_views.route('/signup', methods=["POST"])
def signup():
    if Customer.query.filter_by(email=request.form['email']).first():
        flash("Email is Taken", category="email")
        return redirect('/signup')
    elif Customer.query.filter_by(username=request.form['username']).first():
        flash("Email is Taken", category="username")
        return redirect('/signup')
    elif request.form['password_1'] != request.form['password_2']:
        flash("Passwords do not match", category="password")
        return redirect('/signup')
    else:
        new_customer = Customer(
            firstname = request.form['firstname'],
            lastname = request.form['lastname'],
            email = request.form['email'],
            username = request.form['username'],
            password_hash = generate_password_hash(request.form['password_1'], method='sha256')
        )
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('home_view.home_page'))
