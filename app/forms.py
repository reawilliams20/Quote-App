from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    goal = StringField('Goal', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    submitAI1 = SubmitField('Generate Quote AI1')