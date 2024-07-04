from flask import Blueprint,render_template

user=Blueprint('user',__name__,static_folder='static',template_folder='templates')

@user.route("/")
@user.route("/home")
def home():
    return render_template('index.html')

@user.route("/blog")
def blogs():
    return render_template('blog.html')

@user.route("/payment")
def payment():
    pass