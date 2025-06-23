"""Question 30
● Title: Full System Simulation
● Question: Combine several of the concepts. Create a Farm class. A farm should
have a name, a list of FarmAnimal objects, and a dictionary of Crop objects
(where the key is the field name and the value is the crop object). Write methodsfor the Farm class to:
1. add_animal(animal)
2. plant_crop(field_name, crop)
3. get_daily_report(): A method that printsthe total number of animals and lists
the crops being grown in each field."""

#Title: Full System Simulation
# Animal class
class FarmAnimal:
    def __init__(self, species, weight):
        self.species = species
        self.weight = weight

# Crop class
class Crop:
    def __init__(self, name, yield_per_hectare):
        self.name = name
        self.yield_per_hectare = yield_per_hectare

# Farm class
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.fields = {}

    def add_animal(self, animal):
        self.animals.append(animal)

    def plant_crop(self, field_name, crop):
        self.fields[field_name] = crop

    def get_daily_report(self):
        print(f"Farm Name: {self.name}")
        print(f"\nTotal number of animals: {len(self.animals)}")
        print("\nCrops in fields:")
        for field_name, crop in self.fields.items():
            print(f"  Field '{field_name}' it's crop {crop.name}")
        
# Create a farm
my_farm = Farm("Green Valley Farm")

# Add animals
my_farm.add_animal(FarmAnimal("Cow", 500))
my_farm.add_animal(FarmAnimal("Chicken", 2))

# Plant crops
my_farm.plant_crop("Field A", Crop("Maize", 1500))
my_farm.plant_crop("Field B", Crop("Rice", 2000))

# Get daily report
my_farm.get_daily_report()