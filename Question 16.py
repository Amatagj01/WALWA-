"""Question 16
● Title: Inheritance: Farm Equipment
● Question: Create a base class FarmEquipment with attributes name and
purchase_price. Create two child classes, Tractor and Harvester, that inherit from
FarmEquipment. Add a specific attribute to each child class (horsepower for
Tractor, cutting_width for Harvester). Instantiate one of each and print their
unique attributes."""

#Title: Inheritance: Farm Equipment.
class FarmEquipment:
  def __init__(self, name, purchase_price):
    self.name = name
    self.purchase_price = purchase_price
    
    
class Tractor(FarmEquipment):
    def __init__(self, name, purchase_price, horsepower):
        super().__init__(name, purchase_price)
        self.horsepower = horsepower
        
        
class Harvester(FarmEquipment):
    def __init__(self, name, purchase_price, cutting_width):
        super().__init__(name, purchase_price)
        self.cutting_width = cutting_width
        
tractor1 = Tractor("John Deere 5100", 50000, 120)
harvester1 = Harvester("Claas Lexion", 75000, 3.2)
       

print(f"Tractor: {tractor1.name}, Horsepower: {tractor1.horsepower}")
print(f"Harvester: {harvester1.name}, Cutting Width: {harvester1.cutting_width}")