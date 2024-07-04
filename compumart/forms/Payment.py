from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField,SubmitField
from wtforms.validators import Length,InputRequired,DataRequired


# get payment method selected and its details
class PaymentDetails(FlaskForm):
    
    method=RadioField("select a method of payment.",choices=['CreditCard','Mobile','Paypal','Other'],default='CreditCard')
    
    #credit card
    name=StringField(validators=[Length(min=3),InputRequired('this field is required.'),DataRequired('please fill in this field.')],render_kw={"placeholder":"cardholder's name"})
    card_no=StringField(validators=[Length(min=16),DataRequired('please give a valid card number.'),InputRequired('this field is required.')],render_kw={"placeholder":"cardnumber"})
    date=StringField(validators=[DataRequired('please enter mm/yy.'),InputRequired("this field is required")],render_kw={"placeholder":"MM/YY"})
    cvv=IntegerField(validators=[DataRequired(),InputRequired()],render_kw={"placeholder":"CVV"})
    submit=SubmitField("Make Payment")
    
    # mpesa
    code=StringField("country code",choices=[('KEN','254'),('UGA','256'),('TZA','255'),('RWA','250'),('ETH','251')],default=('KEN','254'),validators=[DataRequired(),InputRequired()])
    phone=StringField(validators=[Length(min=9,max=9)],render_kw={"placeholder":"phone number"})
    submit=SubmitField("Make Payment")
    
    
    
    # paypal
    # coming soon
    
    
    