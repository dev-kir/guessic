from flask import Flask, Blueprint, render_template, redirect, url_for, request
from app.forms import inputForm

main = Blueprint('main', __name__, template_folder='templates')
# home = Blueprint('home', __name__, template_folder='templates')

# @home.route('/')
# def home_route():
#     return render_template('home.html')


@main.route('/', methods = ['GET', 'POST'])
def index():
    form = inputForm()
    if form.validate_on_submit():
        number = form.number.data
        gender = form.gender.data
        print(f"Number: {number}, Gender: {gender}")
        return redirect(url_for('main.index'))
    return render_template('index.html', form = form)

@main.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        # Access form data
        number = request.form.get('number')
        gender = request.form.get('gender')

        # Print the data (you can modify this based on your actual form fields)
        print(f"Number: {number}, Gender: {gender}")

    return render_template('test.html')