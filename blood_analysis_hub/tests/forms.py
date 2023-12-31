from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

def create_testForm(attributes):
    class TestForm(FlaskForm):
        select_attribute = SelectField('Select Attribute', choices=attributes)
        title = StringField('Title', validators=[DataRequired()])
        submit = SubmitField('Add')
        
    return TestForm()