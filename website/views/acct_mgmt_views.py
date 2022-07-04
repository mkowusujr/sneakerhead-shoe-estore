"""
Manages all routes related to account management

Author: Mathew Owusu Jr
"""


from flask import Blueprint, Response, render_template, redirect, request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Customer, Cart
from .. import db

acct_mgmt_views = Blueprint('acct_mgmt_views', __name__)


@acct_mgmt_views.route('/signup', methods=["GET"])
def display_signup_page():
    """
    Displays the signup page

    Returns:
        A rendered HTML template
    """
    return render_template('acct_mgmt/signup.html', 
    current_user=current_user)


@acct_mgmt_views.route('/signup', methods=["POST"])
def signup():
    """
    The business logic for signing up/account creation

    Returns:
        Redirects the page to the home page if the process is successful
        else it redirects back to the signup page
    """
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
    """
    Displays the login page

    Returns:
        A rendered HTML template
    """
    return render_template('acct_mgmt/login.html', 
    current_user=current_user)


@acct_mgmt_views.route('/login', methods=["POST"])
def login():
    """
    The business logic for logging into an account

    Returns:
        Redirects the page to the account management page
    """
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
    """
    Display the a users account information

    Parameters:
        user_id (int): The id of the user being accessed

    Returns:
        A rendered HTML template
    """
    return render_template('acct_mgmt/mg_acct.html', 
    current_user=current_user)


@acct_mgmt_views.route('/logout')
@login_required
def logout():
    """
    Logs the currently signed in user out

    Returns:
        Redirects the page to the display login page
    """
    logout_user()
    return redirect(url_for('acct_mgmt_views.display_login_page'))


@acct_mgmt_views.route('/user/<int:user_id>/email', methods=['PUT'])
@login_required
def change_email(user_id):
    """
    Changes the user email address
    
    Parameters:
        user_id (int): The id of the user being accessed

    Returns:
        HTTP Reponse: Send the url for the display account page and a http status
        of 200 for success
    """
    data = request.get_json()
    user = Customer.query.get_or_404(user_id)
    old_email = data['old_email']
    new_email = data['new_email']
    if old_email == user.email:
        user.email = new_email
        db.session.add(user)
        db.session.commit()
        return Response(url_for('acct_mgmt_views.display_account_page', user_id=user_id), 200)
    else:
        return Response('', 400)



@acct_mgmt_views.route('/user/<int:user_id>/password', methods=['PUT'])
@login_required
def change_password(user_id):
    """
    Changes the user's password

    Parameters:
        user_id (int): The id of the user being accessed

    Returns:
        HTTP Reponse: Send the url for the display account page and a http status
        of 200 for success
    """
    data = request.get_json()
    user = Customer.query.get_or_404(user_id)
    old_passord = data['old_pass']
    new_passord = data['new_pass']
    if check_password_hash(user.password_hash, old_passord):
        user.password_hash = generate_password_hash(new_passord, method='sha256')
        db.session.add(user)
        db.session.commit()
        return Response(url_for('acct_mgmt_views.display_account_page', user_id=user_id), 200)
    else:
        return Response('', 400)


@acct_mgmt_views.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_account(user_id):
    """
    Deletes a user's account

    Parameters:
        user_id (int): The id of the user being accessed

    Returns:
        HTTP Reponse: Send the url for the display signup page and a http status
        of 200 for success
    """
    user = Customer.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return Response(url_for('acct_mgmt_views.display_signup_page'), 200)
