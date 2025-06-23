"""Question 24
● Title: Polymorphism: Machine Maintenance
● Question: Have a Machine base class with a perform_maintenance() method.
Create WaterPump and Generator child classes that override this method to
provide specific maintenance steps. Write a function
service_machine(machine_object) that takes any machine object and calls its
perform_maintenance() method. Demonstrate this function with both a
WaterPump and a Generator object."""

#Title: Polymorphism: Machine Maintenance
# Base class
class Machine:
    def perform_maintenance(self):
        print("Performing general machine maintenance.")

# Child class: WaterPump
class WaterPump(Machine):
    def perform_maintenance(self):
        print("Clean the filter and check valve seals in the water pump.")

# Child class: Generator
class Generator(Machine):
    def perform_maintenance(self):
        print("Change oil and inspect spark plugs in the generator.")

# Function to demonstrate polymorphism
def service_machine(machine_object):
    machine_object.perform_maintenance()
    
    # Create machine objects
pump = WaterPump()
gen = Generator()

# Call maintenance function
service_machine(pump)
service_machine(gen)