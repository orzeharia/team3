import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify
from utilities.db.pizzaTable import Pizza

gallery = Blueprint('gallery', __name__,
                     static_folder='static',
                     static_url_path='/gallery/static',
                     template_folder='templates')


@gallery.route('/gallery')
def main():
    pizza = Pizza()
    allPizza = pizza.getAllPizza()
    return render_template('gallery.html',allPizza=allPizza)
