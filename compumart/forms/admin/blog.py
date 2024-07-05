from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,FileField,SubmitField
from wtforms.validators import DataRequired,InputRequired
from flask_wtf.file import FileRequired,FileAllowed


class Blog(FlaskForm):
    
    title=StringField(validators=[DataRequired('please put in a title for the blog.'),InputRequired('this field is required.')],render_kw={"placeholder":"blog title here eg.All about the latest gaming laptops"})
    blog=TextAreaField(validators=[DataRequired('please put in blog content'),InputRequired('this field is required')],render_kw={"placeholder":"put in blog content"})
    image=FileField("choose image",FileRequired(),FileAllowed(['png','jpg','jpeg']))
    submit=SubmitField("post blog")
    
    