"""Question 10
 ● Title: Irrigation Water Consumption
● Question: Represent a weekly irrigation schedule using a dictionary where keys
are days of the week and values are the duration of irrigation in minutes. Write a
program to calculate the total water consumed in a week, assuming a constant
flow rate of 20 liters per minute."""

#Title: Irrigation Water Consumption
weekly_irrigation = {
  "Monday": 600,
  "Tuesday":450,
  "Wednesday":560,
  "Thursday": 420,
  "Friday":344,
  "Saturday":300,
  "Sunday":0
}

#for the total water consumed in a week.
total_minuts = sum(weekly_irrigation.values())

total_water = (total_minuts)*20

print("The total water consumed in the week it is",total_water ,"liters per minute.")
