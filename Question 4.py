"""Question 4
● Title: Soil pH Analysis with NumPy
● Question: A NumPy array stores soil pH values from 10 different locations in a
field: ph_values = np.array([6.2, 6.5, 5.8, 7.1, 6.0, 5.5, 6.8, 6.3, 5.9, 6.6]).
Write a script to:
1. Find the average pH.
2. Count the number of locations with acidic soil (pH < 6.0).
3. Create a new array categorizing each value as 'Acidic', 'Neutral' (6.0 <= pH <=7.0), or 'Alkaline' (pH > 7.0)."""
# Title: Soil pH Analysis with NumPy
import numpy as np

# Soil pH values from 10 locations
ph_values = np.array([6.2, 6.5, 5.8, 7.1, 6.0, 5.5, 6.8, 6.3, 5.9, 6.6])

# 1. Find the average pH
average_pH = np.mean(ph_values)
print("1. The average soil pH is:", average_pH)

# 2. Count the number of locations with acidic soil (pH < 6.0)
acidic_count = np.sum(ph_values < 6.0)
print("2. Number of acidic locations (pH < 6.0):", acidic_count)

# 3. Categorize each value as 'Acidic', 'Neutral', or 'Alkaline'
categories = []
for ph in ph_values:
    if ph < 6.0:
        categories.append('Acidic')
    elif 6.0 <= ph <= 7.0:
        categories.append('Neutral')
    else:
        categories.append('Alkaline')

# Convert to NumPy array for consistency (optional)
categories = np.array(categories)
print("3. Soil pH Categories:", categories)