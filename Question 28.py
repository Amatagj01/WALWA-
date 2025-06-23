"""Question 28
● Title: Inheritance & Polymorphism: Pest Management
● Question: Create a base class Pest with a damage_report method. Create two
child classes, InsectPest and FungalPest, which override this method. Then,
create a Crop class that has a list for storing pest objects that are affecting it.
Write a method in the Crop class called generate_pest_report that iterates
through its list of pests and calls the damage_report method for each one."""

#Title: Inheritance & Polymorphism: Pest Management.
# Base class: Pest
class Pest:
    def damage_report(self):
        print("Pest damage report not specified.")

# InsectPest subclass
class InsectPest(Pest):
    def damage_report(self):
        print("Leaves have holes due to insect feeding.")

# FungalPest subclass
class FungalPest(Pest):
    def damage_report(self):
        print("White spots on leaves indicate fungal infection.")
        
class Crop:
    def __init__(self, name):
        self.name = name
        self.pests = []  # list of Pest objects

    def add_pest(self, pest):
        self.pests.append(pest)

    def generate_pest_report(self):
        print(f"Pest report for {self.name}:")
        for pest in self.pests:
            pest.damage_report()
  
# Create pests
insect = InsectPest()
fungus = FungalPest()

# Create crop and add pests
maize = Crop("Maize")
maize.add_pest(insect)
maize.add_pest(fungus)

# Generate pest report
maize.generate_pest_report()