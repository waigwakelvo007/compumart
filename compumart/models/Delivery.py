# delivery and billing address
from compumart import db
from datetime import datetime


class Delivery(db.Model):
    __tablename__='delivery'
    
    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(300),unique=True)
    # who the delivery is for.This is gotten from orders table so that we can match the right order to its delivery depending on who 
    # made the order
    customer=db.Column(db.Integer,db.ForeignKey('orders.customer'),unique=True)
    item=db.Column(db.String,db.ForeignKey('orders.code'),nullable=False,default='no item')
    depature_time=db.Column(db.DateTime,nullable=False,default='not set')
    arrival_time=db.Column(db.DateTime)
    
    
    # initialization
    def __init__(self,address,depature_time,arrival_time):
        
        self.address=address
        self.depature_time=depature_time
        self.arrival_time=arrival_time
        
    # get all the deliveries made
    def get_all(cls):
        
        deliveries=cls.query.all()
    
        return deliveries
    
    
    # get id
    def get_id(self):
        id=self.id
        
        return id