from flask import Blueprint,render_template
from .forms.RepairQuote import RepairQuote
from .forms.review import Review
from .forms.Payment import CreditCard,Mobile
from .forms.Customer import Customer

user=Blueprint('user',__name__,static_folder='static',template_folder='templates')

@user.route("/")
@user.route("/home")
def home():
    review=Review()
    return render_template('index.html',form=review)

@user.route("/blog")
def blogs():
    return render_template('blog.html')

@user.route("/payment")
def payment():
    creditcard=CreditCard()
    mobile=Mobile()
    return render_template('payment.html',form_mobile=mobile,form_card=creditcard)


@user.route("/repair-services")
def repair_services():
    repair_quote=RepairQuote()
    return render_template('repair.html',form=repair_quote)