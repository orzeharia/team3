import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

FAQs = Blueprint('FAQs', __name__,
                 static_folder='static',
                 static_url_path='/FAQs',
                 template_folder='templates')


@FAQs.route('/contact_us')
def main():
    return render_template('contact_us.html')
