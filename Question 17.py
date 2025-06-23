"""Question 17
● Title: Inheritance: Crop Types
● Question: Create a base class Crop with a planting_instructions() method that
prints a generic message. Create two child classes, CerealCrop and LegumeCrop,
that inherit from Crop and have their own specific attributes (e.g., grain_type for
Cereal, nitrogen_fixing boolean for Legume)."""

#Title: Inheritance: Crop Types.
# Base class
class Crop:
    def planting_instructions(self):
        print("Plant in well-prepared soil with adequate sunlight.")

# Child class: CerealCrop
class CerealCrop(Crop):
    def __init__(self, grain_type):
        self.grain_type = grain_type

# Child class: LegumeCrop
class LegumeCrop(Crop):
    def __init__(self, nitrogen_fixing):
        self.nitrogen_fixing = nitrogen_fixing
        
        
  # Create one CerealCrop and one LegumeCrop
maize = CerealCrop("Maize")
beans = LegumeCrop(True)

# Call inherited method and print specific attributes
print("Cereal Crop Information:")
maize.planting_instructions()
print(f"Grain Type: {maize.grain_type}")

print("\nLegume Crop Information:")
beans.planting_instructions()
print(f"Nitrogen Fixing: {beans.nitrogen_fixing}")     







