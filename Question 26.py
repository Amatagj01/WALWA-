"""Question 26
● Title: Farm Management System: Classes
● Question: Design a Field class that contains a list of Crop objects (use the Crop
class from a previous question). The Field class should have an attribute
size_in_hectares and a method get_total_yield() that iterates through its crops
and calculates a total estimated yield (you can add a yield_per_hectare attribute
to your Crop class)."""

#Title: Farm Management System: Classes
# Crop class from earlier
class Crop:
    def __init__(self, name, yield_per_hectare):
        self.name = name
        self.yield_per_hectare = yield_per_hectare  # in kg per hectare

# Field class
class Field:
    def __init__(self, size_in_hectares):
        self.size_in_hectares = size_in_hectares
        self.crops = []  # List to store Crop objects

    def add_crop(self, crop):
        self.crops.append(crop)

    def get_total_yield(self):
        total_yield = 0
        for crop in self.crops:
            total_yield += crop.yield_per_hectare * self.size_in_hectares
        return total_yield
        
        
# Create crops
maize = Crop("Maize", 1500)      # 1500 kg/ha
beans = Crop("Beans", 800)       # 800 kg/ha

# Create a field of 2 hectares
field = Field(2)

# Add crops to the field
field.add_crop(maize)
field.add_crop(beans)

# Calculate total yield
print("Total estimated yield from field:", field.get_total_yield(), "kg")