from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField,SubmitField
from wtforms.validators import Length,InputRequired




class MethodOfPayment(FlaskForm):
    method=RadioField("select a method of payment.",choices=[('CreditCard','CreditCard'),('Mobile','Mobile'),('Paypal','Paypal'),('Other','Other')],default='CreditCard',validators=[InputRequired()])
    submit=SubmitField("")
    
    
# get payment method selected and its details
# credit card
class CreditCard(FlaskForm):
    
    name=StringField(validators=[Length(min=3),InputRequired()],render_kw={"placeholder":"cardholder's name"})
    card_no=StringField(validators=[Length(min=16),InputRequired()],render_kw={"placeholder":"cardnumber"})
    date=StringField(validators=[InputRequired()],render_kw={"placeholder":"MM/YY"})
    cvv=IntegerField(validators=[InputRequired()],render_kw={"placeholder":"CVV"})
    submit=SubmitField("Make Payment")
  
  
# mpesa  
class Mobile(FlaskForm):
    code=RadioField("country code",choices=[('KEN 254','KEN 254'),('UGA 256','UGA 256'),('TZA 255','TZA 255'),('RWA 250','RWA 250'),('ETH 251','ETH 251')],validators=[InputRequired()])
    phone=StringField(validators=[Length(min=9,max=9),InputRequired()],render_kw={"placeholder":"phone number"})
    submit=SubmitField("Make Payment")
    
    
# paypal
# coming soon
class Paypal(FlaskForm):
    pass
    
    
    
    
    
    
    