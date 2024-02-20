from flask import Blueprint, render_template, redirect, url_for
from app.forms import inputForm

main = Blueprint('main', __name__, template_folder='templates')
# home = Blueprint('home', __name__, template_folder='templates')
# about = Blueprint('about', __name__, template_folder='templates')
# contact = Blueprint('contact', __name__, template_folder='templates')

# @home.route('/')
# def home_route():
#     return render_template('home.html')

# @about.route('/about')
# def about_route():
#     return render_template('about.html')

# @contact.route('/contact')
# def contact_route():
#     return render_template('contact.html')

@main.route('/', methods = ['GET', 'POST'])
def index():
    form = inputForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('index.html', form = form)

@main.route('/test')
def test():
    return render_template('test.html')