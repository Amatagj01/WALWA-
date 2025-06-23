"""Question 21
● Title: Polymorphism: Farm Vehicle Operation
● Question: Create a parent class FarmVehicle with a method start_engine().
Create child classes Tractor and CombineHarvester. Override the start_engine()
method in each child class to print a specific sound (e.g., "Tractor engine rumbles
to life," "Harvester engine whirs loudly."). Create a list containing one object of
each child class and loop through it, calling the start_engine() method for each
vehicle."""

#Title: Polymorphism: Farm Vehicle Operation.
# Base class
class FarmVehicle:
    def start_engine(self):
        print("Farm vehicle engine starting...")

# Child class: Tractor
class Tractor(FarmVehicle):
    def start_engine(self):
        print("Tractor engine roars to life.")

# Child class: CombineHarvester
class CombineHarvester(FarmVehicle):
    def start_engine(self):
        print("Harvester engine whirs loudly.")
        
      
# Create vehicle objects
tractor = Tractor()
harvester = CombineHarvester()

# Store in a list
vehicles = [tractor, harvester]

# Loop and call start_engine (Polymorphism in action)
for vehicle in vehicles:
    vehicle.start_engine()