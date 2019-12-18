from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddWeightForm(FlaskForm):
    weight = TextAreaField('Enter weight', validators=[DataRequired()])
    submit = SubmitField('Submit')