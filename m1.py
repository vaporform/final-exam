class Person:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")
    
class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.address = address
    
    ### JHERE!
    def place_order(self,item):
        return DeliveryOrder(c,item)
    
class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self,order):
        # NTS: ORDER IS DELIVERY ORDER!
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")
        order.status = "delivered"
    
class DeliveryOrder:
    def __init__(self,c,i):
        self.customer = c
        self.item = i
        self.status = "preparing"
    
    def assign_driver(self,driver):
        driver.deliver()
    
    def summary(self):
        l = f'Item: {self.item}\nCustomer: {self.customer.name}\nStatus: {self.status}'
        return l
    
# MAIN
c1 = Customer("Alice","A1")
c2 = Customer("Bob","B2")
d = Driver("David","motorcycle")
c1.introduce()
c2.introduce()
d.introduce()
print()
do1 = DeliveryOrder(c1,'Laptop')
do2 = DeliveryOrder(c2,'Headphones') 

# DONT FORGET TO CHECK THE DO1 DO2!
print(do1.summary())
print()
print(do2.summary())

