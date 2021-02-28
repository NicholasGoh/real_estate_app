from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

class AllPersonalInfo(FlaskForm):
    avgIncome = FloatField('Average Gross Salary', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(21, 100, 'Enter valid age!')])
    noOfRooms = IntegerField('Number of Rooms', validators=[DataRequired(), NumberRange(1, 5, 'Enter valid number of rooms!')])
    firstTime = BooleanField('First timer?')
    relationship = SelectField('Relationship', validators=[Optional()], choices=[('Single First Timer', 'Single First Timer'), ('Single Second Timer', 'Single Second Timer'), ('First Timer Couple', 'First Timer Couple'), ('Second Timer Couple', 'Second Timer Couple'), ('First Timer with Singapore Permanent Resident Spouse', 'First Timer with Singapore Permanent Resident Spouse'), ('First Timer with Second Timer Spouse', 'First Timer with Second Timer Spouse')])
    employment = BooleanField('Currently under employment?')
    remainingLease = IntegerField('Remaining Lease', validators=[DataRequired()])
    appliedForFlat = BooleanField('Have you applied for a flat?')
    submit = SubmitField('Submit')
