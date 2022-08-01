import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for, session
from utilities.db.user import User


login = Blueprint('login', __name__,
                    static_folder='static',
                    static_url_path='/login',
                    template_folder='templates')


@login.route('/login')
def main():
    return render_template('log_in.html')


@login.route('/log_in/<message>/<message_type>')
def log_in(message, message_type):
    if message:
        flash(message, message_type)
    return render_template('log_in.html')


@login.route('/login_user', methods=['post'])
def login_user():
    email = request.form['email']

    user = User()
    found_user = user.search_user(email)

    if found_user:
        password=[]
        username=[]
        email=[]
        for user in found_user:
            password.append(user.password)
            username.append(user.username)
            email.append(user.email)

        if password[0] == request.form['password']:
            session['username'] = username[0]
            session['email'] = email[0]
            session['loggedin'] = True
            return render_template('home.html', username=username[0])

        else:
            flash("Wrong Password", "warning")

    else:
        flash("User Email Does Not Exist", "danger")

    return redirect('/login')


@login.route("/logout/", methods=['POST'])
def log_out():
    session['loggedin'] = False
    session.clear()
    return redirect('/home')
