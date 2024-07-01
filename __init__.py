# initialization file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from admin import admin

app=Flask(__name__)
db=SQLAlchemy(app)


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite3:///compumart.db"
db.init_app(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


app.register_blueprint(admin,url_prefix='/admin')
