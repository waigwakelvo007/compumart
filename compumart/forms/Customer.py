from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,SubmitField
from wtforms.validators import Length,InputRequired,DataRequired

# customer details
class Customer(FlaskForm):
    
    firstname=StringField(validators=[Length(min=3),InputRequired()],render_kw={"placeholder":"firstname"})
    lastname=StringField(validators=[Length(min=3),InputRequired()],render_kw={"placeholder":"lastname"})
    mobile_code=RadioField(choices=[('KEN','254'),('UGA','256'),('TZA','255'),('RWA','250'),('ETH','251')],render_kw={"placeholder":"country code"})
    phone_number=StringField(validators=[Length(min=9,max=9),InputRequired()],render_kw={"placeholder":"phonenumber"})
    address=StringField(validators=[InputRequired()],render_kw={"placeholder":"delivery address"})
    remember_me=BooleanField("save my details for faster processing when i order next.")
    submit=SubmitField("Continue")


