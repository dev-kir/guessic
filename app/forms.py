from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class inputForm(FlaskForm):
    number = StringField(
        'Number', 
        validators = [
            DataRequired(),
            Length(min = 8, max = 8, message='Number must be 8 digits'),
            Regexp('^\d+$', message = 'Only numbers are allowed.')
        ]
    )
    gender = RadioField(
        'Gender', 
        choices = [
            ('male', 'MALE'),
            ('female', "FEMALE")
        ],
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField(
        'Submit'
    )