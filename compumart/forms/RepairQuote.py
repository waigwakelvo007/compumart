from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Length,InputRequired,DataRequired,Email


# form for getting a repair quote
class RepairQuote(FlaskForm):
    
    name=StringField(validators=[InputRequired(),Length(min=3)],render_kw={"placeholder":"Your name."})
    email=StringField(validators=[InputRequired(),Email()],render_kw={"placeholder":"Your email."})
    issue=TextAreaField(validators=[InputRequired()],render_kw={"placeholder":"Describe your issue here."})
    submit=SubmitField("Get a Quote")
    