from compumart import db
from Products import Product


# ==========================================PAYMENT METHODS===============================================================


# various payment methods that can be used
class Payment_methods(db.Model):
    __tablename__='payment_methods'
    
    id=db.Column(db.Integer,primary_key=True)
    method=db.Column(db.String(100),nullable=False,default='credit card')
    
    
    def __init__(self,method):
        
        self.method=method
        
    
    
    def __repr__(self):
        return f"id:{self.id},payment method:{self.method}"
    
    
    # get all payment methods
    def get_all(cls):
        payment_methods=cls.query.all()
        return payment_methods
    
    

#===================================================PAYMENTS====================================================================
 
    
# details of the payments made
class Payment(db.Model):
    __tablename__="payment"
    
    id=db.Column(db.Integer,primary_key=True)
    method=db.Column(db.String(100),db.ForeignKey('payment_methods.method'),nullable=False,default='Visa')
    # payment for the specific order,since it could be the same customer but different orders
    order=db.Column(db.String(300),db.ForeignKey('orders.code'))
    amount=db.Column(db.Integer,nullable=False)
    status=db.Column(db.String(50),nullable=False,default="not paid")
    transaction_code=db.Column(db.String(300),nullable=True)
    received_from=db.Column(db.String(300),nullable=True)
    
    
    def __init__(self,method,order,amount,status,transaction,received_from):
        
        self.method=method
        self.product=order
        self.amount=amount
        self.status=status
        self.transaction_code=transaction
        self.received_from=received_from
    
        
    def __repr__(self):
        return f"method:{self.method},customer:{self.customer},amount:{self.amount},status:{self.status}"
        
        
    # get all payments
    def get_all(cls):
        
        payments=cls.query.all()
        return payments
    
    # get id of payment
    def get_id(self):
        
        id=self.id
        return id
    
