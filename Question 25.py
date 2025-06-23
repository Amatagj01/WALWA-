"""Question 25
● Title: Overriding: Harvesting Methods
● Question: Create a Plant class with a method harvest(). Create FruitTree (which
overrides harvest to say "Harvest by picking fruits carefully") and RootVegetable
(which overrides harvest to say "Harvest by digging up from the soil") subclasses.
Show that calling harvest() on a list containing objects of both subclasses results in different behaviors."""

#Title: Overriding: Harvesting Methods.
# Base class
class Plant:
    def harvest(self):
        print("Harvesting the plant.")

# Child class: FruitTree
class FruitTree(Plant):
    def harvest(self):
        print("Harvest by picking fruits carefully.")

# Child class: RootVegetable
class RootVegetable(Plant):
    def harvest(self):
        print("Harvest by digging up from the soil.")
        
        
# Create plant objects
apple_tree = FruitTree()
carrot = RootVegetable()

# Store in list
plants = [apple_tree, carrot]

# Loop and call harvest (polymorphism in action)
for plant in plants:
    plant.harvest()
    