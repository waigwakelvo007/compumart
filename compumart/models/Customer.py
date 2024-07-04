# customer details
from compumart import db


class Customer(db.Model):
    __tablename__='customer'
    
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(150))
    lastname=db.Column(db.String(150))
    phone=db.Column(db.String(100),unique=True)
    delivery_address=db.Column(db.String(300))
    
    
    def __init__(self,firstname,lastname,phone,delivery_address):
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.delivery_address=delivery_address
        
        
    def __repr__(self):
        return f"firstname:{self.firstname},lastname:{self.lastname},phone:{self.phone}"
    
    
    def get_all(cls):
        customers=cls.query.all
        
        return customers