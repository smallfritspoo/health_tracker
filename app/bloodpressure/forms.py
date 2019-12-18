from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class AddBloodPressureForm(FlaskForm):
    systolic = IntegerField('Enter Systolic Pressure', validators=[DataRequired()])
    diastolic = IntegerField('Enter Diastolic Pressure', validators=[DataRequired()])
    taken = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField('Submit')

