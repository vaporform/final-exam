# Project Delivery Time
A basic OOP-style program that helps manage your customers, orders and drivers!

# Features
The program currently can do the following:
## Customer
- Create customers with names and addresses

## Driver
- Create drivers with names and vehicles
- Deliver assigned orders
## DeliveryOrder
- Create orders with customer information, item and status.
- Assign drivers for each order
- Create order summaries

# Limitations
Currently, all classes does not have input validation built in, so beware!

# How to run
Before running, check that Python is installed in your system by running the command in terminal:
```
python3 --version
```
If Python has already been installed, you can download the repository directly or clone it by running:
```
git clone https://github.com/vaporform/final-exam.git
```
Open the folder via prefered IDE or in the terminal
```
cd final_exam
```
Then run the command
```
python3 main.py
```
# Project structure
```
final_exam/
│
├── Example_Result.png  (An example output from main.py)
├── helper.py  (A file that contains all of neccessary classes: Person, Customer, Driver and DeliveryOrder)
├── main.py (Main file to run the code)
└── README.md (This file)
```