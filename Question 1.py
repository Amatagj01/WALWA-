""""
  Question 1
● Title: Crop Yield Data Analysis
● Question: A list contains the maize yield (in tonnes) from a university farm for the
past ten years: yield_data = [3.5, 4.2, 3.9, 4.5, 5.1, 4.8, 5.5, 5.3, 5.8, 6.2].
Write a Python program to:
1. Calculate the average yield.
2. Find the year with the highest and lowest yield (by value).
3. Determine the number of years the yield was above 5.0 tonnes."""
 #Crop Yield Data Analysis 
     
#Maize yield in tonnes from the university farm for the past ten years

yield_data = [3.5, 4.2, 3.9, 4.5, 5.1, 4.8, 5.5, 5.3, 5.8, 6.2]
count = 0
total = 0
highest_yield = 0
lowest_yield = 0
Year = 0
 

# 1. Average yield 
total = sum(yield_data)
average = total /len(yield_data)
print("The average yield of Maize for the past ten years is:",average)
print("______________________________________________________")

# Step 2:Years with highest and lowest Maize yield
# 2.i: The year with lowest Maize yield.
for data in yield_data:
  lowest_data = yield_data[0]
  if data < lowest_data:
    lowest_data = data
lowest_data_index = yield_data.index(lowest_data)
lowest_data_index +=1
print("The year with lowest Maize yield data is year",lowest_data_index)

print("_______________________________________________________")

#Step2. ii: The Year with highest Maize yield data 
for data in yield_data: 
  highest_data = yield_data[0]
  if data > highest_data:
    highest_data = data
highest_data_index = yield_data.index(highest_data)
highest_data_index +=1
print("The year with highest Maize yield data is year", highest_data_index)

print("________________________________________________________")  
#.3.Number of years the yield was above 5.0 tonnes 

for data in yield_data:
  if data > 5:
    data = data
    count +=1 
print("The number of years in which the Maize yield was above 5.0 tonnes are:",count,"years")
  
print("______________________________________________________")
 







