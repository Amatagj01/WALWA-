"""Question 22
● Title: Overriding: Animal Feeding
● Question: Create a Livestock class with a feed() method that prints "This animal
eats generic food." Create Cow and Chicken child classes that override the feed()
method to specify their diet (e.g., "Cow is eating fresh grass and silage," "Chicken
is pecking at grains and corn."). Demonstrate polymorphism by calling the feed()
method on a list of these animal objects."""

#Title: Overriding: Animal Feeding
# Base class
class Livestock:
    def feed(self):
        print("This animal eats generic food.")

# Child class: Cow
class Cow(Livestock):
    def feed(self):
        print("Cow is eating fresh grass and silage.")

# Child class: Chicken
class Chicken(Livestock):
    def feed(self):
        print("Chicken is pecking at grains and corn.")# Create animal objects
cow = Cow()
chicken = Chicken()

# Store in a list
animals = [cow, chicken]

# Loop and feed each animal (polymorphism in action)
for animal in animals:
    animal.feed()
    