from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

# custom web form for financial schemes
class AllPersonalInfo(FlaskForm):
    avgIncome = FloatField('Average Gross Salary', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(21, 100, 'Enter valid age!')])
    noOfRooms = IntegerField('Number of Rooms', validators=[DataRequired(), NumberRange(1, 5, 'Enter valid number of rooms!')])
    firstTime = SelectField('First timer?', validators=[Optional()], choices=[('',''), ('Yes', 'Yes'), ('No', 'No')])
    relationship = SelectField('Relationship', validators=[Optional()], choices=[('',''), ('Single First Timer', 'Single First Timer'), ('Single Second Timer', 'Single Second Timer'), ('First Timer Couple', 'First Timer Couple'), ('Second Timer Couple', 'Second Timer Couple'), ('First Timer with Singapore Permanent Resident Spouse', 'First Timer with Singapore Permanent Resident Spouse'), ('First Timer with Second Timer Spouse', 'First Timer with Second Timer Spouse')])
    employment = SelectField('Currently under employment?', validators=[Optional()], choices=[('',''), ('Yes', 'Yes'), ('No', 'No')])
    remainingLease = IntegerField('Remaining Lease', validators=[DataRequired()])
    appliedForFlat = SelectField('Have you applied for a flat?', validators=[Optional()], choices=[('',''), ('Yes', 'Yes'), ('No', 'No')])
    loan = SelectField('Are you planning to take a loan?', validators=[DataRequired()], choices=[('',''), ('No loan', 'No loan'), ('HDB Housing loan', 'HDB Housing loan'), ('Bank loan', 'Bank loan')])
    submit = SubmitField('Submit')
