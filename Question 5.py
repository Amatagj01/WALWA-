"""Question 5
● Title: Tractor Fuel Cost Log
● Question: A list contains the daily fuel consumption (in liters) of a tractor:
fuel_log = [45.5, 52.0, 48.3, 42.1, 55.6]. If the price of diesel is 2,800 TZS per liter,
calculate the total fuel cost for the recorded period"""

#Title: Tractor Fuel Cost Log

fuel_log = [45.5, 52.0, 48.3, 42.1, 55.6]
price_diesel_TZS = 2800
total_fuel_cost = []
fuel = 0
#The total fuel cost for the recorded period.
for fuel in fuel_log:
  fuel = fuel * 2800
  total_fuel_cost.append(fuel)
print("The  fuel_log cost consumption (in liters) of the tractor is:", total_fuel_cost)
print(f"The Total fuel cost consumption of the Tractor for the recorded period is {sum(total_fuel_cost)} TZS per liter")


 