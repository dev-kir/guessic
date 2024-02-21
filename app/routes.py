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
        number = int(form.number.data)
        gender = form.gender.data
        processed_lines = []
        for i in range(10000):
            line = f"{number:08d}{i:04d}"
            if (gender == 'male' and i % 2 != 0) or (gender == 'female' and i % 2 == 0):
                # line = str(int(line) + 1)
                processed_lines.append(line)
        result_data = '\n'.join(processed_lines)
        return render_template('result.html', result_data=result_data)
    return render_template('index.html', form = form)

@main.route('/test')
def test():
    return render_template('test.html')