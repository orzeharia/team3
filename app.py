from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.home.home import home
app.register_blueprint(home)

## About
from pages.about.about import about_us
app.register_blueprint(about_us)

## FAQs
from pages.FAQs.FAQs import FAQs
app.register_blueprint(FAQs)

## gallery
from pages.gallery.gallery import gallery
app.register_blueprint(gallery)

## my account
from pages.myAccount.myAccount import my_account
app.register_blueprint(my_account)

## orders
from pages.orders.orders import orders
app.register_blueprint(orders)

## sign up
from pages.signUp.signUp import sign_up
app.register_blueprint(sign_up)

## login
from pages.login.login import login
app.register_blueprint(login)


# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)
#
#
# ###### Components
# ## Main menu
# from components.main_menu.main_menu import main_menu
# app.register_blueprint(main_menu)
