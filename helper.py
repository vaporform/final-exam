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
        self.__driver = None #????

    def assign_driver(self,driver):
        # Assuming that the assign driver creates a self.driver. 
        # This is for accessing the driver in summary.
        self.__driver = driver
    
    def summary(self):
        l = f'Item: {self.item}\nCustomer: {self.customer.name}\nStatus: {self.status}\nDriver: {self.__driver.name}'
        return l