from __init__ import db
import datetime
from sqlalchemy import JSON


# ======================================================STORE PRODUCTS================================================================

class Products(db.Model):
    __tablename__='products'
    
    product_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    product_code=db.Column(db.String(100),nullable=False)
    product_name=db.Column(db.String(100))
    image=db.Column(db.LargeBinary)
    image2=db.Column(db.LargeBinary)
    image3=db.Column(db.LargeBinary)
    price=db.Column(db.Integer)
    category=db.Column(db.String(150))
    sub_category=db.Column(db.String(150))
    brand=db.Column(db.String(150))
    description=db.Column(db.String(500))
    attributes=db.Column(JSON)
    availability=db.Column(db.String(150))
    
    def __init__(self,product_code,product_name,image,image2,image3,price,category,brand,description,attributes,availability):
        
        self.product_code=product_code
        self.product_name=product_name
        self.image=image
        self.image2=image2
        self.image3=image3
        self.price=price
        self.category=category
        self.brand=brand
        self.description=description
        self.attributes=attributes
        self.availability=availability
        
    def __repr__(self):
        return f"product:{self.product_name},price:{self.price},type:{self.type},brand:{self.brand}"
    
    # get all products
    def get_all(cls):
        products=cls.query.all()
        return products
    
    
    def get_id(self):    
        id=self.product_id
        return id
     
    
    # get current data
    def data(self):
        
        
        return {
            
            "product_id":self.product_id,
            "product_code":self.product_code,
            "product_name":self.product_name,
            "image":self.image or self.image2 or self.image3,
            "price":self.price,
            "type":self.type,
            "brand":self.brand,
            "short_description":self.short_description,
            "description":self.description,
            "availability":self.availability
        }
        
        
#  ===================================================REPAIR SERVICES===========================================================================       # 
  
  
    
class Services(db.Model):
    __tablename__='services'
    
    service_id=db.Column(db.Integer,primary_key=True,nullable=False)
    service_type=db.Column(db.String(200))
    image=db.Column(db.LargeBinary)
    image2=db.Column(db.LargeBinary)
    image3=db.Column(db.LargeBinary)
    
    description=db.Column(db.String(300))
    price=db.Column(db.Integer)
    
    
    def __init__(self,service_type,image,image2,image3,price,description):
        
        self.service_type=service_type
        self.image=image
        self.image2=image2
        self.image3=image3
        self.price=price
        self.description=description

        
    def __repr__(self):
        return f"product:{self.service_type},price:{self.price},type:{self.type},brand:{self.description}"
    
    
    # get all products
    def get_all(cls):
        services=cls.query.all()
        return services
    
    
    def get_id(self):    
        id=self.service_id
        return id
     
    
    # get current data
    def data(self):
        
        
        return {
            
            "service type":self.service_type,
            "product_id":self.service_id,
            "image":self.image or self.image2 or self.image3,
            "price":self.price,
            "description":self.description,
        }
        
        
#===================================CUSTOMER DETAILS============================================================================================= 
 
   
    
class Customers(db.Model):
    __tablename__='customers'
    
    customer_id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(50))
    phonenumber=db.Column(db.String(80))
    email=db.Column(db.String(150))
    
    
    def __init__(self,firstname,lastname,phonenumber,email):
        
        self.firstname=firstname
        self.lastname=lastname
        self.phonenumber=phonenumber
        self.type=email
        

        
    def __repr__(self):
        return f"product:{self.firstname},price:{self.lastname},type:{self.phonenumber},brand:{self.email}"
    
    
    # get all customers
    def get_all(cls):
        customers=cls.query.all()
        return customers
    
    
    def get_id(self):    
        id=self.customer_id
        return id
     
    
    # get current data
    def data(self):
        
        
        return {
            
            "firstname":self.firstname,
            "lastname":self.lastname,
            "phonenumber":self.phonenumber,
            "email":self.email
            
        }
    
    
#=======================================================DELIVERY DETAILS=========================================================================
 
       
    
class Delivery(db.Model):
    __tablename__='delivery'
    
    delivery_id=db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    delivery_code=db.Column(db.String(100),unique=True,nullable=False)
    order_code=db.Column(db.String(150),db.ForeignKey('order.order_code'),unique=True,nullable=False)
    location=db.Column(db.String(200))
    transit_cost=db.Column(db.Integer)
    starttime=db.Column(db.DateTime,default=datetime.datetime.utcnow)
    delivery_time=db.Column(db.DateTime,default=datetime.datetime.utcnow) 
     
    
    def __init__(self,delivery_code,order_code,location,transit_cost,starttime,delivery_time):
        
        self.delivery_code=delivery_code
        self.order_code=order_code
        self.location=location
        self.transit_cost=transit_cost
        self.starttime=starttime
        self.delivery_time=delivery_time
        

        
    def __repr__(self):
        return f"product:{self.delivery_code},price:{self.order_code},type:{self.location},brand:{self.transit_cost}"
    
    
    # get all deliveries
    def get_all(cls):
        deliveries=cls.query.all()
        return deliveries
    
    
    def get_id(self):    
        id=self.delivery_id
        return id
     
    
    # get current data
    def data(self):
        
        
        return {
            
            "delivery code":self.delivery_code,
            "order code":self.order_code,
            "location":self.location,
            "transit_cost":self.transit_cost,
            "starttime":self.starttime,
            "delivery_time":self.delivery_time,
        

        }
        
        
# ============================================================ORDER DETAILS=================================================================   
    
    
class Order(db.Model):
    __tablename__='order'
    
    order_id=db.Column(db.Integer,primary_key=True,unique=True)
    order_code=db.Column(db.String(150),nullable=False,unique=True)
    product_code=db.Column(db.Integer,db.ForeignKey('products.product_code'),nullable=False,unique=True)
    customers_id=db.Column(db.Integer,db.ForeignKey('client.customer_id'),nullable=False,unique=True)
    delivery_code=db.Column(db.String(150),db.ForeginKey('delivery.delivery_code'),unique=True,nullable=False)
    status=db.Column(db.String(100),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.utcnow)
    
    
    def __init__(self,order_code,product_code,customers_id,delivery_code,status,created_at):
        
        self.order_code=order_code
        self.product_code=product_code
        self.customer_id=customers_id
        self.delivery_code=delivery_code
        self.status=status
        self.created_at=created_at
        

        
    def __repr__(self):
        return f"order code:{self.order_code},product code:{self.product_code},customer id:{self.customer_id},delivery code:{self.delivery_code},status:{self.status},created at:{self.created_at}"
    
    
    # get all deliveries
    def get_all(cls):
        orders=cls.query.all()
        return orders
    
    
    def get_id(self):    
        id=self.order_id
        return id
     
    
    # get current data
    def data(self):
        
        
        return {
            
        "order code":self.order_code,
        "product code":self.product_code,
        "customer id":self.customer_id,
        "delivery code":self.delivery_code,
        "status":self.status,
        "created at":self.created_at
       

        }
        
        
        
# ====================================================PAYMENT DETAILS===========================================================================================



class PaymentDetails(db.Model):
        __tablename__='paymentdetails'
        
        id=db.Column(db.Integer,primary_key=True)
        
        method=db.Column(db.String(150),nullable=False,default='Visa') #eg Paypal
        customer=db.Column(db.Integer,db.ForeignKey('customers.customer_id'))
        transaction_code=db.Column(db.String(150),nullable=True)
        amount=db.Column(db.Float,nullable=False)
        from_client=db.Column(db.String(300),nullable=False) #client account that made payment
        to_account=db.Column(db.String(300)) #account to which payment was made
        currency=db.Column(db.String(150)) #eg USD,Ksh
        status=db.Column(db.String) #eg successful,failed,incomplete
        payment_date=db.Column(db.Datetime,nullable=False,default=datetime.datetime.utcnow)
        last_updated=db.Column(db.DateTime,nullable=False,default=datetime.datetime.utcnow) #upon completion of payment if status was incomplete before
        
        
        def __init__(self,method,customer,transaction_code,amount,from_client,to_account,currency,status,payment_date):
        
            self.method=method,
            self.customer=customer,
            self.transaction_code=transaction_code,
            self.amount=amount,
            self.from_client=from_client,
            self.to_account=to_account,
            self.currency=currency,
            self.status=status,
            self.payment_date=payment_date
            
            
        def __repr__(self):
            return f"method_of_payment:{self.method},transaction code:{self.transaction_code},amount:{self.amount},currency:{self.currency},status:{self.status},payment date:{self.payment_date}"
    
    
        # get all payment detail entries
        def get_all(cls):
            payment_details=cls.query.all()
            return payment_details
        
        
        def get_id(self):    
            id=self.id
            return id
        
        
        # get payment details
        def data(self):
            
            
            return {
                
            "method":self.method,
            "customer":self.customer,
            "transaction code":self.transaction_code,
            "amount":self.amount,
            "from client":self.from_client,
            "to account":self.to_account,
            "currency":self.currency,
            "status":self.status,
            "payment date":self.payment_date

            }
            
    
    

 