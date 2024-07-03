from flask import *
from models import *


admin=Blueprint("admin",__name__,static_folder='static',template_folder='template')


@admin.route("/home")
@admin.route("/")
def home():
    return render_template('admin_index.html')


# upload content into the web
@admin.route('',methods=['GET','POST'])
def upload_content():
    pass
    


