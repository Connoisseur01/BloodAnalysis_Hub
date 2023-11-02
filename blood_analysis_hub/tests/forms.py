from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    hb = IntegerField('Hemoglobin', validators=[DataRequired()])
    hct = IntegerField('Hematocrit', validators=[DataRequired()])
    rbc = IntegerField('Red Blood Cell Count', validators=[DataRequired()])
    wbc = IntegerField('White Blood Cell Count', validators=[DataRequired()])
    pc = IntegerField('Platelet Count', validators=[DataRequired()])
    mcv = IntegerField('Mean Corpuscular Volume', validators=[DataRequired()])
    mch = IntegerField('Mean Corpuscular Hemoglobin', validators=[DataRequired()])
    mchc = IntegerField('Mean Corpuscular Hemoglobin Concentration', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add')