"""Question 2
● Title: Fertilizer Cost Calculation
● Question: You have a list of recommended nitrogen fertilizer application rates (in
kg/ha) for different soil types: rates = [120, 150, 100, 180, 130]. The farm has 5
fields, each corresponding to a rate in the list. If the cost of fertilizer is 1,500 TZS
per kg, create a new list containing the total fertilizer cost for each one-hectare
field."""

rates = [120, 150, 100, 180, 130]
total_fertilizer_cost =[]
field = 5
cost_per_kg_in_TZS = 1500 

for rate in rates:
  rate = rate * 1500
  total_fertilizer_cost.append(rate)
print("The new list containing the total fertilizer cost for each one-hectare of the 5 fields is: Total fertilizer cost = ",total_fertilizer_cost)