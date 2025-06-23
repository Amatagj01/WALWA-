"""Question 11
● Title: Tractor Object Modeling
● Question: Create a Tractor class with attributes model, horsepower, and
fuel_capacity. Include a method display_info() that prints all the attributes in a
readable format. Create an object of the Tractor class for a "Massey Ferguson
240" and call the display_info() method."""

#Title: Tractor Object Modeling

class Tractor:
  def __init__(self ,model ,horsepower ,fuel_capacity): 
   self.model = model 
   self.horsepower = horsepower
   self.fuel_capacity = fuel_capacity
   
  def display_info(self):
    print(f"Model: {self.model}")
    print(f"Horsepower: {self.horsepower}")
    print(f"Fuel Capacity: {self.fuel_capacity} liters")
 
my_tractor = Tractor("Massey Ferguson 240" ,70 ,60)

my_tractor.display_info()
 
 