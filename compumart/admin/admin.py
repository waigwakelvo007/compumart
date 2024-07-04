from flask import Blueprint,render_template


admin=Blueprint("admin",__name__)

# pages that the web owner can manage his website
@admin.route("/")
@admin.route("/home")
def home():
    return render_template('admin/index.html')

