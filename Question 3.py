"""Question 3
● Title: Weekly Rainfall Analysis
● Question: A list stores the daily rainfall measurements (in mm) for a week: rainfall
= [10.2, 0.0, 5.5, 1.2, 8.0, 0.0, 3.5]. Write a program to calculate the total weekly
rainfall and identify the days with no rainfall (e.g., "Day 2", "Day 6")."""

#Weekly Rainfall Analysis
rainfall = [10.2, 0.0, 5.5, 1.2, 8.0, 0.0, 3.5,] 
total = 0
count = 0
total = sum(rainfall)
print("The total weekly rainfall is ",total)

for rain_days in rainfall:
  if rain_days == 0:
   count += 1
print("The days with no rainfall in a week are",count,"days")
rain_days_index = rainfall.index(rain_days==0)
rain_days_index +=1
print("The days with no rainfall is day",rain_days_index)
rain_days_index = rainfall.index(rain_days)
print("and day",rain_days_index)
  

