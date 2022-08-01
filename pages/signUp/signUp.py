import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from utilities.db.user import User


sign_up = Blueprint('sign_up', __name__,
                    static_folder='static',
                    static_url_path='/sign_up',
                    template_folder='templates')


@sign_up.route('/sign_up')
def main():
    return render_template('sign_up.html')



@sign_up.route('/create_user', methods=['post'])
def create_user():
    password = request.form['password']
    verify = request.form['verifyPassword']
    email = request.form['email']

    user = User()

    if password != verify:
        flash("Passwords Do Not Match", "warning")

    else:
        searched_user = user.search_user(email)
        if searched_user:
            print(searched_user)
            flash("User Email already exists", "danger")

        else:
            user_added = user.add_user(request.form['email'], request.form['username'], request.form['birthdate'],
                          request.form['password'])

            return redirect(url_for('login.log_in', message="User Created Successfully!", message_type="success"))

    return redirect('/sign_up')






# Creates an instance for the User class for export.
#user = User()
