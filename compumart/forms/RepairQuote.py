from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Length,InputRequired,DataRequired,Email


# form for getting a repair quote
class RepairQuote(FlaskForm):
    
    name=StringField(validators=[Length(min=3),DataRequired(),InputRequired('please provide details here.')],render_kw={"placeholder":"Your name."})
    email=StringField(validators=[DataRequired(),Email(),InputRequired('please provide details here.')],render_kw={"placeholder":"Your email."})
    issue=TextAreaField(validators=[DataRequired(),InputRequired('please provide details here.')],render_kw={"placeholder":"Describe your issue here."})
    get_quote=SubmitField("Get a Quote")
    