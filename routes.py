from flask import redirect,url_for,render_template,session,request
from __init__ import *


@app.route('/home',methods=['POST','GET'])
@app.route('/')
def home():
    return render_template('index.html')

# view products
@app.route('/product')
def product():
    return render_template('product.html')

# view cart and its items
@app.route('/cart')
def cart():
    return render_template('cart.html')

# checkout form store
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')