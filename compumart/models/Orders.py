# all the orders made 
from compumart import db
from datetime import datetime
from sqlalchemy import JSON


class Orders(db.Model):
    __tablename__='orders'
    
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    code=db.Column(db.String(300),unique=True)
    # all the products in the order and its subtotal
    products=db.Column(JSON,nullable=False)
    subtotal=db.Column(db.Integer,nullable=False)
    customer=db.Column(db.String(150),db.ForeignKey('customer.id'),nullable=False,unique=True)
    at_time=db.Column(db.DateTime,nullable=False,default=datetime.now)
    # status of whether payment was made or not.From payment tables
    status=db.Column(db.String,db.ForeignKey('payment.status'))
    
    
    def __init__(self,code,customer,at_time,status):
        
        self.code=code
        self.customer=customer
        self.at_time=at_time
        self.status=status
        
        
    # get all orders
    def get_all(cls):
        orders=cls.query.all()
        
        return orders
    
    
    # unique identifiers which are the product code and id
    def get_uniqueid(self):
        code=self.code
        id=self.id
        
        return [code,id]
    
    
    
        