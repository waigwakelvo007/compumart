from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .admin.admin import admin
from .user import user
import secrets


# initialize the flask app
app=Flask(__name__)
secret_key=secrets.token_hex(24)


# app configurations
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///compumart.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["SEND_FILE_MAX_AGE_DEFAULT"]=0
app.config["SECRET_KEY"]=secret_key

# imitialize database
db=SQLAlchemy(app)


# register blueprints
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/")


# import routes
from . import user
print(app.jinja_loader.list_templates())
