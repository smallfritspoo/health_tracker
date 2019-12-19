from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import IntegerField, DateField


class AddMetabolicPanel(FlaskForm):
    sodium = IntegerField('Na Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    calcium = IntegerField('Ca Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    chloride = IntegerField('Cl Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    potassium = IntegerField('K Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    magnesium = IntegerField('Mg Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    blood_urea_nitrogen = IntegerField('BUN Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    creatinine = IntegerField('Cr Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    glucose = IntegerField('GLUC Value', validators=[NumberRange(min=0, max=100000), DataRequired()])
    timestamp = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField('Submit Metabolic Panel')


class AddCompleteBloodCellCount(FlaskForm):
    white_blood_cell_count = IntegerField('WBC value', validators=[NumberRange(min=0, max=500000), DataRequired()])
    hemoglobin = IntegerField('Hb value', validators=[NumberRange(min=0, max=20), DataRequired()])
    hematocrit = IntegerField('HCT value', validators=[NumberRange(min=0, max=100), DataRequired()])
    platelet = IntegerField('PLT value', validators=[NumberRange(min=0, max=1000000), DataRequired()])
    timestamp = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField('Submit CBC Values')