from flask import Flask, Blueprint, render_template, redirect, url_for, request
from app.forms import inputForm

main = Blueprint('main', __name__, template_folder='templates')
# home = Blueprint('home', __name__, template_folder='templates')

# @home.route('/')
# def home_route():
#     return render_template('home.html')


@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', form = inputForm())

@main.route('/result', methods = ['GET', 'POST'])
def result():
    form = inputForm()
    if form.validate_on_submit():
        number = form.number.data
        gender = form.gender.data
        result_data = (f"Number: {number}, Gender: {gender}")
        # process data here

        return render_template('result.html', result_data=result_data)
    return render_template('index.html', form = form)

@main.route('/test')
def test():
    return render_template('test.html')