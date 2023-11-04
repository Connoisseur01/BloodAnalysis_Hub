from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class TestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    
    # Complete blood count (CBC)
    # Red blood cells
    hb = DecimalField('Hemoglobin (Hb)', places=2, rounding=None, validators=[DataRequired()])
    hct = IntegerField('Hematocrit (Hct)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    rbc = IntegerField('Red Blood Cell Count (RBC)', validators=[DataRequired()])
    # Red blood cell indices
    mcv = DecimalField('Mean Corpuscular Volume (MCV)', places=2, rounding=None, validators=[DataRequired()])
    mch = DecimalField('Mean Corpuscular Hemoglobin (MCH)', places=2, rounding=None, validators=[DataRequired()])
    mchc = DecimalField('Mean Corpuscular Hemoglobin Concentration (MCHC)', places=2, rounding=None, validators=[DataRequired()])
    # white blood cells
    wbc = IntegerField('White Blood Cell Count', validators=[DataRequired()])
    # Platelets
    pc = IntegerField('Platelet Count', validators=[DataRequired()])
    
    submit = SubmitField('Add')