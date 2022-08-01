import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for, session
from datetime import datetime

from utilities.db.orderTable import Order
from utilities.db.user import User


my_account = Blueprint('my_account', __name__,
                       static_folder='static',
                       static_url_path='/my_account',
                       template_folder='templates')


@my_account.route('/my_account')
def main():
    order = Order()
    user = User()
    email = session['email']
    found_user = user.search_user(email)
    birthday = found_user[0].birthday
    datetimeObject = birthday
    today = datetime.now()
    delta1 = datetime(today.year, datetimeObject.month, datetimeObject.day)
    delta2 = datetime(today.year+1, datetimeObject.month, datetimeObject.day)
    days = ((delta1 if delta1 > today else delta2) - today).days
    points = found_user[0].points
    allOrders = order.search_order(email)
    name = session['username']
    return render_template('my_account.html',days=days, points=points, allOrders=allOrders, name=name)


@my_account.route('/my_account/loggedOut')
def mainLoggedOut():
    return render_template('my_account.html')


@my_account.route('/update_user', methods=['post'])
def update_user():
    user = User()
    prev_email = session['email']
    found_user = user.search_user(prev_email)

    if found_user:
        prev_password = []
        prev_username = []
        prev_email = []
        for found in found_user:
            prev_password.append(found.password)
            prev_username.append(found.username)
            prev_email.append(found.email)
        prev_username = prev_username[0]
        prev_email = prev_email[0]
        prev_password = prev_password[0]

        if request.form['username']:
            new_username = request.form['username']
        else:
            new_username = prev_username

        if request.form['email']:
            new_email = request.form['email']
        else:
            new_email = prev_email

        if request.form['password']:
            new_password = request.form['password']
        else:
            new_password = prev_password

        user_updated = user.update_user(new_email, new_username, new_password, prev_email)
        session['email'] = new_email
        session['username'] = new_username

        flash("User Updated", "success")

    return redirect('/my_account')




@my_account.route('/delete_user', methods=['post'])
def delete_user():
    user = User()
    email = session['email']
    user_deleted = user.delete_user(email)
    session['loggedin'] = False
    session.clear()
    flash("User Deleted", "success")

    return redirect('/home')

