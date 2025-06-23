"""Question 12
● Title: Crop Growth Cycle Class
● Question: Define a Crop class with attributes name, planting_date, and
days_to_maturity. Add a method calculate_harvest_date() that calculates and
returns the expected harvest date (you can use Python's datetime and timedelta
objects)."""

#Title: Crop Growth Cycle Class  
  
from datetime import datetime, timedelta

class Crop:
    def __init__(self, planting_date, days_to_maturity):
        self.planting_date = planting_date  # planting_date is a datetime object
        self.days_to_maturity = days_to_maturity

    def calculate_harvest_date(self):
        harvest_date = self.planting_date + timedelta(days=self.days_to_maturity)
        return harvest_date.strftime("%Y-%m-%d")  # returns the date in "YYYY-MM-DD" format

# Example usage
planting_date_str = "2025-06-10"
planting_date = datetime.strptime(planting_date_str, "%Y-%m-%d")
days_to_maturity = 90

my_crop = Crop(planting_date, days_to_maturity)
harvest_date = my_crop.calculate_harvest_date()
print("The Harvesting Date is :", harvest_date)