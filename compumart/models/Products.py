from compumart import db
from sqlalchemy import JSON

class Product(db.Model):
    __tablename__='products'
    
    id=db.Column(db.Integer,unique=True,primary_key=True)
    code=db.Column(db.String(150),unique=True)
    name=db.Column(db.String(300),nullable=False)
    description=db.Column(db.String(1200))
    price=db.Column(db.Integer,nullable=False,default=0.00)
    attributes=db.Column(JSON)
    category=db.Column(db.String(100),nullable=False)
    sub_category=db.Column(db.String(100))
    image=db.Column(db.LargeBinary)
    image2=db.Column(db.LargeBinary)
    image3=db.Column(db.LargeBinary)
    
    
    # initializing instance
    def __init__(self,code,name,description,price,attributes,image,image2,image3):
        
        self.code=code
        self.name=name
        self.description=description
        self.price=price
        self.attributes=attributes
        self.image=image
        self.image2=image2
        self.image3=image3
        
    
    # get all instances
    def get_all(cls):
        
        products=cls.query.all()
        return products
    
    # print out of the object
    def __repr__(self):
        return f"product code:{self.code},name:{self.name},attributes:{self.attributes},price:{self.price}"
    
    
    # id of the object
    def get_id(self):
        id=self.id
        return id
    
    
    # get json format of product
    def get_json(self):
        return {
            
            "name":self.name,
            "code":self.code,
            "price":self.price,
        }
    
    

