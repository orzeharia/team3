from datetime import date, datetime

import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify, session, flash

from utilities.db.orderTable import Order
from utilities.db.pizzaTable import Pizza
from utilities.db.user import User

orders = Blueprint('orders', __name__,
                   static_folder='static',
                   static_url_path='/orders',
                   template_folder='templates')


@orders.route('/Order_qestions')
def main():
    return render_template('Order_qestions.html')


@orders.route('/order')
def order():
    return render_template('order.html')


@orders.route('/OrderConfirmation')
def OrderConfirmation():
    return render_template('OrderConfirmation.html', free=False)


@orders.route('/pizza_cal', methods=['post'])
def pizzaCal():
    season = request.form['season']
    continent = request.form['continent']
    meal = request.form['meal']
    count = 0
    if (season == "winter"):
        count = count + 1

    if (season == "summer"):
        count = count + 2

    if (season == "Fall"):
        count = count + 3

    if (season == "Spring"):
        count = count + 4

    if (continent == "America"):
        count = count + 5
    if (continent == "Asia"):
        count = count + 6
    if (continent == "Australia"):
        count = count + 7
    if (continent == "Europe"):
        count = count + 8
    if (continent == "Antarctica"):
        count = count + 9
    if (meal == "yes"):
        count = count + 10

    if (meal == "no"):
        count = count + 11

    pizza = Pizza()
    allPizza = pizza.getAllPizza()
    gap = 50
    res = 0
    for pizza in allPizza:
        if abs(pizza.score - count) < gap:
            res = pizza
            gap = abs(pizza.score - count)
    session['pizzaRes'] = res
    return render_template('order.html', name=res.name, price=res.price, description=res.description,picture=res.picture,alt=res.alt)

@orders.route('/pizza_del', methods=['post'])
def pizzaDel():
    numPizza =request.form['num']
    deliveryPizza =20
    Pizza=session['pizzaRes']
    price=int(Pizza[2])
    resPrice_delivery=int(numPizza)*price+deliveryPizza
    session['total_price'] = resPrice_delivery
    session['numPizza'] = numPizza


    if session.get('email'):
        if session['email']:
            user = User()
            points = user.get_points(session['email'])
            birthday=user.get_birthday(session['email'])
            today=datetime.today()

            if birthday.month == today.month and birthday.day == today.day:
                is_birthday = True
            else:
                is_birthday = False

            return render_template('order.html', numPizza=numPizza, RES=resPrice_delivery, name=Pizza[1], price=Pizza[2],
                                   description=Pizza[3], picture=Pizza[4], alt=Pizza[5], points=points, birthday=is_birthday)
    else:
        return render_template('order.html', numPizza=numPizza, RES=resPrice_delivery, name=Pizza[1], price=Pizza[2], description=Pizza[3],picture=Pizza[4],alt=Pizza[5])




@orders.route('/submit_order', methods=['post'])
def submitOrder():
    order=Order()
    user=User()

    email = request.form['email']
    time = request.form['time']
    address = request.form['address']
    tel=request.form['tel']
    numPizza=session['numPizza']
    total_price=session['total_price']
    pizza=session['pizzaRes']
    name=pizza[1]

    if request.form['free'] == 'False':
        creditNum=request.form['creditNum']
        CVV=request.form['CVV']
        expDate = request.form['expDate']

        if len(CVV) != 3 or CVV.isdigit() == False:
            flash('CVV must be 3 digits', 'warning')
            return render_template('orderConfirmation.html', free=False)

        elif len(creditNum) < 10 or len(creditNum) > 16 or creditNum.isdigit() == False:
            flash('Invalid credit card number', 'warning')
            return render_template('orderConfirmation.html', free=False)


        order.add_order(email,time,address,tel,name,numPizza,total_price,creditNum,expDate,CVV)
        flash('Your order has been placed and will be delivered soon', 'success')


        user_found = user.search_user(email)
        if user_found:
            user_email = email
            points_to_add = total_price * 0.1
            user.add_points(points_to_add, user_email)

        elif session.get('loggedin'):
            if session['loggedin']:
                user_email = session['email']
                points_to_add = total_price * 0.1
                user.add_points(points_to_add, user_email)


    else:
        order.add_order(email, time, address, tel, name, numPizza, total_price, None, '0000-00-00', None)
        flash('Your free pizza order has been placed and will be delivered soon', 'success')


    return render_template('home.html')




@orders.route('/free_pizza', methods=['post'])
def free_pizza():
    user = User()
    user_email = session['email']
    pizza_price = session['total_price']
    user.use_points(user_email, pizza_price)
    return render_template('OrderConfirmation.html', free=True)


@orders.route('/birthday_pizza', methods=['post'])
def birthday_pizza():
    user = User()
    user_email = session['email']
    return render_template('OrderConfirmation.html', free=True)
