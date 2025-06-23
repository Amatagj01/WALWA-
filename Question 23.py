"""Question 23
● Title: Overriding: Crop Water Needs
● Question: Create a Crop class with a method get_water_needs() that returns a
generic string "Requires regular watering." Create child classes Sugarcane and
Sorghum that override this method to return more specific water needs (e.g.,
"Requires high water volume," "Is drought-resistant, requires minimal water.")."""

#Title: Overriding: Crop Water Needs.
# Base class
class Crop:
    def get_water_needs(self):
        return "Requires regular watering."

# Child class: Sugarcane
class Sugarcane(Crop):
    def get_water_needs(self):
        return "Requires high water volume."

# Child class: Sorghum
class Sorghum(Crop):
    def get_water_needs(self):
        return "Is drought-resistant, requires minimal water."
 
# Create crop objects
sugarcane = Sugarcane()
sorghum = Sorghum()

# Print water needs
print("Sugarcane:", sugarcane.get_water_needs())
print("Sorghum:", sorghum.get_water_needs())       