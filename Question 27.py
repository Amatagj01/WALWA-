""""Question 27
● Title: Data Management: Dictionaries and Classes
● Question: Create a program that uses a dictionary to manage multiple Tractor
objects (use the Tractor class). The dictionary keys should be the tractor's
registration plate number (e.g., 'T 123 SUA'), and the values should be the tractor
objects. Write a function to look up a tractor by its plate number and display its
horsepower."""
 #Title: Data Management: Dictionaries and Classes
# Tractor class
class Tractor:
    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower
        
        
# Dictionary of tractors
tractor_inventory = {
    "T 123 SUA": Tractor("John Deere 5100", 120),
    "T 456 TZA": Tractor("Massey Ferguson 290", 95),
    "T 789 UCA": Tractor("New Holland T6", 150)
}

def lookup_tractor(plate_number):
    if plate_number in tractor_inventory:
        tractor = tractor_inventory[plate_number]
        print(f"The Tractor is: {tractor.name}")
        print(f"The Tractor Horsepower is: {tractor.horsepower} HP")
    else:
        print("Tractor not found in the inventory.")   
        
  # Test lookup
lookup_tractor("T 123 SUA")  # Exists
lookup_tractor("T 250 ABC")  # Not found  
lookup_tractor("T 456 TZA") 