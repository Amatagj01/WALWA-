"""Question 7
● Title: Crop Nutrient Lookup
● Question: A dictionary stores nutrient requirements (in kg/ha) for crops:
crop_nutrients = {'Maize': {'N': 120, 'P': 60, 'K': 60}, 'Rice': {'N': 100, 'P': 50, 'K':
50}}. Write a program that allows a user to input a crop name and a nutrient (e.g.,
'P') and prints the required amoun"""

#Title: Crop Nutrient Lookup
crop_nutrients = {
    'Maize': {'N': 120, 'P': 60, 'K': 60},
    'Rice': {'N': 100, 'P': 50, 'K': 50}
}

# User input
crop_name = input("Enter the crop name as Maize or Rice: ").strip().title()
nutrient = input("Enter the nutrient as N, P or K: ").strip().upper()

# Logic to validate input and display result
if crop_name in crop_nutrients:
    if nutrient in crop_nutrients[crop_name]:
        print(f"The {crop_name} crop requires {crop_nutrients[crop_name][nutrient]} kg/ha of {nutrient}.")
    else:
        print("Invalid nutrient name.")
else:
    if nutrient not in ['N', 'P', 'K']:
        print("Both crop name and nutrient name are invalid.")
    else:
        print("Invalid crop name.")
  
  
  
  

 