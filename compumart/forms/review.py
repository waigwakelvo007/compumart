from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,InputRequired


# review form 
class Review(FlaskForm):
    
    name=StringField(validators=[InputRequired(),Length(min=3)],render_kw={"placeholder":"Your name"})
    title=StringField(validators=[Length(min=5),InputRequired()],render_kw={"placeholder":"eg.Student,Businessman."})
    institution=StringField(validators=[Length(min=5),InputRequired()],render_kw={"placeholder":"Institution or organisation."})
    review=StringField(validators=[InputRequired()],render_kw={"placeholder":"Your review here."})
    submit=SubmitField("Post")
    
    
    