import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

home = Blueprint('home', __name__,
                 static_folder='static',
                 static_url_path='/home',
                 template_folder='templates')

@home.route('/')
@home.route('/home')
def main():
    return render_template('home.html')