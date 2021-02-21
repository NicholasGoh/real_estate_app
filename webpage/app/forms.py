from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange

class AllPersonalInfo(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(21, 100, 'Enter valid age!')])
    salary = FloatField('Average Gross Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')
