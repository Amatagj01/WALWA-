"""Question 20
● Title: Inheritance: Livestock
● Question: Define a parent class Livestock with attributes species and weight.
Create child classes Cattle and Poultry inheriting from Livestock. Add a method
calculate_feed_ratio() to each child class that returns a feed amount based on
weight (e.g., cattle: weight * 0.02, poultry: weight * 0.05)."""

#Title: Inheritance: Livestock.
# Base class
class Livestock:
    def __init__(self, species, weight):
        self.species = species
        self.weight = weight

# Child class: Cattle
class Cattle(Livestock):
    def __init__(self, species, weight):
        super().__init__(species, weight)

    def calculate_feed_ratio(self):
        return self.weight * 0.02

# Child class: Poultry
class Poultry(Livestock):
    def __init__(self, species, weight):
        super().__init__(species, weight)

    def calculate_feed_ratio(self):
        return self.weight * 0.05
 
# Create objects
cow = Cattle("Cow", 500)
chicken = Poultry("Chicken", 2.5)

# Print feed required
print(f"The {cow.species} with Weight of {cow.weight} kg, it need  : {cow.calculate_feed_ratio()} kg of Feeds")
print(f"The {chicken.species} with Weight of {chicken.weight} kg, it need  : {chicken.calculate_feed_ratio()} kg of Feeds")