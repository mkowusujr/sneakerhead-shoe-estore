from flask import Blueprint, Response, render_template, redirect, request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Customer, Cart
from .. import db

acct_mgmt_views = Blueprint('acct_mgmt_views', __name__)


@acct_mgmt_views.route('/signup', methods=["GET"])
def display_signup_page():
    return render_template('acct_mgmt/signup.html', 
    current_user=current_user)


@acct_mgmt_views.route('/signup', methods=["POST"])
def signup():
    if Customer.query.filter_by(email=request.form['email']).first():
        flash("Email is Taken", category="email")
        return redirect('/signup')
    elif request.form['password_1'] != request.form['password_2']:
        flash("Passwords do not match", category="password")
        return redirect('/signup')
    else:
        new_customer = Customer(
            firstname = request.form['firstname'],
            lastname = request.form['lastname'],
            email = request.form['email'],
            password_hash = generate_password_hash(request.form['password_1'], method='sha256')
        )
        db.session.add(new_customer)
        # db.session.commit()
        user_cart = Cart()
        db.session.add(user_cart)

        new_customer.cart = user_cart
        db.session.add(new_customer)

        db.session.commit()
        login_user(new_customer, remember=True)
        return redirect(url_for('home_view.home_page'))

@acct_mgmt_views.route('/login', methods=["GET"])
def display_login_page():
    return render_template('acct_mgmt/login.html', 
    current_user=current_user)


@acct_mgmt_views.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    user = Customer.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('home_view.home_page'))
    return redirect(url_for('acct_mgmt_views.login'))


@acct_mgmt_views.route('/user/<int:user_id>', methods=['GET'])
@login_required
def display_account_page(user_id):
    return render_template('acct_mgmt/mg_acct.html', 
    current_user=current_user)


@acct_mgmt_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('acct_mgmt_views.display_login_page'))


@acct_mgmt_views.route('/user/<int:user_id>/email', methods=['PUT'])
@login_required
def change_email(user_id):
    pass


@acct_mgmt_views.route('/user/<int:user_id>/password', methods=['PUT'])
@login_required
def change_password(user_id):
    pass

@acct_mgmt_views.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_account(user_id):
    user = Customer.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return Response(url_for('acct_mgmt_views.display_signup_page'), 200)
