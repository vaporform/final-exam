from helper import *
# MAIN
# CREATE A CUSTOMER INSTANCE
c1 = Customer("Alice","A1")
c2 = Customer("Bob","B2")
# CREATE A DRIVER INSTANCE
d = Driver("David","motorcycle")
# TRY INTRODUCING
c1.introduce()
c2.introduce()
d.introduce()
print()
# CREATE A DELIVERY ORDER: CUSTOMER, ITEM
do1 = DeliveryOrder(c1,'Laptop')
do2 = DeliveryOrder(c2,'Headphones') 
# ASSIGN A DRIVER TO EACH ORDER.
do1.assign_driver(d)
do2.assign_driver(d)
# TELL THE ORDER SUMMARY
print("Order Summary:")
print(do1.summary())
print()
print("Order Summary:")
print(do2.summary())
print()
# DELIVER ORDERS
d.deliver(do1)
d.deliver(do2)
print()
print("Final Status:")
# GET ITEM AND STATUS OF EACH ORDER
print(f"Order for {do1.item} → {do1.status}")
print(f"Order for {do2.item} → {do2.status}")