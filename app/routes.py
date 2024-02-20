from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='templates')
about = Blueprint('about', __name__, template_folder='templates')
contact = Blueprint('contact', __name__, template_folder='templates')

@home.route('/')
def home_route():
    return render_template('home.html')

@about.route('/about')
def about_route():
    return render_template('about.html')

@contact.route('/contact')
def contact_route():
    return render_template('contact.html')