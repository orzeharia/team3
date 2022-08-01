import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

about_us = Blueprint('about_us', __name__,
                     static_folder='static',
                     static_url_path='/about',
                     template_folder='templates')


@about_us.route('/about_us')
def main():
    return render_template('about_us.html')
