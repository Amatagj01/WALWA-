"""Question 13
● Title: Soil Sample Analysis Class
● Question: Create a SoilSample class with attributes sample_id, ph_level, and
organic_matter_content (as a percentage). Include a method get_fertility_status()
that returns the string 'High' if pH is between 6.0-7.0 and organic matter > 2.5%,
'Medium' if only one condition is met, and 'Low' otherwise."""

#Title: Soil Sample Analysis Class.


class Soil_sample:
   def __init__(self, sample_id, ph_level, organic_matter_content):
     self.sample_id = sample_id
     self.ph_level = ph_level
     self.organic_matter_content = organic_matter_content
     
   def get_fertility_status(self):
    pH = 6.0 <= self.ph_level <= 7.0
    Organic = self.organic_matter_content > 2.5

    if pH and Organic:
        return "High"
    elif pH or Organic:
        return "Medium"
    else:
        return "Low"

# Get user input
sample_id = input("Enter sample ID: ")
ph_input = input("Enter pH level (e.g., 6.5): ")
om_input = input("Enter organic matter content in % (e.g., 2.8): ")

# Convert input to float
try:
    ph_level = float(ph_input)
    organic_matter_content = float(om_input)

    # Create the SoilSample object
    sample = Soil_sample(sample_id, ph_level, organic_matter_content)

    # Get and print the fertility status
    status = sample.get_fertility_status()
    print(f"\nSample ID: {sample.sample_id}")
    print(f"pH Level: {sample.ph_level}")
    print(f"Organic Matter Content: {sample.organic_matter_content}%")
    print(f"Fertility Status: {status}")

except ValueError:
    print(" Invalid input. Please enter numeric values for pH and organic matter.")   
   
    
  