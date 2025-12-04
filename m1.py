class Person:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")
    
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
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"
    
class DeliveryOrder:
    def __init__(self,c,i):
        self.customer = c
        self.item = i
        self.status = "preparing"
        self.driver = None #????

    def assign_driver(self,driver):
        # Assuming that the assign driver creates a self.driver. 
        # This is for accessing the driver in summary.
        self.driver = driver
    
    def summary(self):
        l = f'Item: {self.item}\nCustomer: {self.customer.name}\nStatus: {self.status}\nDriver: {self.driver.name}'
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
do1.assign_driver(d)
do2.assign_driver(d)
# DONT FORGET TO CHECK THE DO1 DO2! ##NY DRIVER!
print("Order Summary:")
print(do1.summary())
print()
print("Order Summary:")
print(do2.summary())
print()
d.deliver(do1)
d.deliver(do2)
print()
print("Final Status:")
print(f"Order for {do1.item} → {do1.status}")
print(f"Order for {do2.item} → {do2.status}")