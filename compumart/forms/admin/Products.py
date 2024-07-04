from flask_wtf import FlaskForm
from wtforms import SelectField,RadioField,StringField,IntegerField,TextAreaField
from wtforms.validators import Email,DataRequired,InputRequired,Length
from flask_wtf.file import FileRequired,FileField,FileAllowed


class Product(FlaskForm):
    
    name=StringField(validators=[DataRequired(),InputRequired()],render_kw={"placeholder":"Product name eg.HP Pavilion 11th Gen intel i5"})
    code=StringField(validators=[DataRequired()],render_kw={"placeholder":"product code i.e unique numeric value on product"},default="null")
    
    # if this is selected,a barcode image scan is used instead and code field is disabled
    use_barcode=RadioField("use barcode instead.",validators=[DataRequired()])
    
    # barcode scan image file
    barcode=FileField('barcode',validators=[FileRequired(),FileAllowed(['png','jpg','jpeg'],'image only!')])
    
    # product images
    image1=FileField(validators=[FileRequired(),FileAllowed(['png','jpeg','jpg'])])
    image2=FileField(validators=[FileRequired(),FileAllowed(['png','jpeg','jpg'])])
    image3=FileField(validators=[FileRequired(),FileAllowed(['png','jpeg','jpg'])]) 
    
    # category and subcategory that the image falls under
    category=RadioField('choose a category the item falls under.',choices=[('Desktops','Desktops'),('Laptops','Laptops'),('Smartphones','Smartphones'),('Printers and Scanners','Printers and Scanners'),('Softwares','Softwares'),('Accesories','Accessories'),('Speakers and Sound Systems','Speakers and Sound Systems')])
    # to be continued..
    sub_categories=RadioField()   
    
    # description of products
    description=TextAreaField(render_kw={"placeholder":"""give a description of the product eg it has a RAM of 8gb and SSD storage 256gb 
                                    and high resulotion screen"""},validators=[DataRequired('please give a description of the product.'),InputRequired('this field is required'),Length(min=300)])
    price=IntegerField(render_kw={"placeholder":"unit price"},validators=[DataRequired('please give the price of the product.'),InputRequired('this field is required.')])
    