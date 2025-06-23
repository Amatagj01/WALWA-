"""Question 14
● Title: Farm Animal Class
● Question: Design a FarmAnimal class with attributes for species, age, and
purpose (e.g., 'Dairy', 'Meat'). Add a method get_details() that returns a formatted
string with all the animal's information. Create two different animal objects and
print their details."""

#Title: Farm Animal Class
class FarmAnimal:
  def __init__(self, species, age, purpose):
    self.species = species 
    self.age = age
    self.purpose = purpose
    
  def get_details(self):
    return f"""Species: {self.species}
Age: {self.age} years
Purpose: {self.purpose}"""

species = input("Enter animal species: ")
age = int(input("Enter animal age in years: "))
purpose = input("Enter animal purpose (Dairy/Meat): ")

user_animal = FarmAnimal(species, age, purpose)
print("The Farm Animal Details:")
print(user_animal.get_details())