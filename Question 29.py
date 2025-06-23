"""Question 29
● Title: Abstract Class & Inheritance: Water Management
● Question: Define an abstract class WaterSource with an abstract method
get_water(liters). Create two concrete classes: Borehole (which has a
max_daily_extraction limit) and River (which has a flow_rate). Implement the
get_water method in each to simulate drawing water, accounting for their specific
constraints."""
 #Title: Abstract Class & Inheritance: Water Management.
from abc import ABC, abstractmethod

# Abstract base class
class WaterSource(ABC):
    def get_water(self, liters):
        pass
class Borehole(WaterSource):
    def __init__(self, max_daily_extraction):
        self.max_daily_extraction = max_daily_extraction

    def get_water(self, liters):
        if liters > self.max_daily_extraction:
            return "Request exceeds daily borehole limit!"
        else:
            return f"{liters} liters extracted from borehole."
            
class River(WaterSource):
    def __init__(self, flow_rate):  # flow_rate in liters per second
        self.flow_rate = flow_rate

    def get_water(self, liters):
        time_required = liters / self.flow_rate
        return f"{liters} liters will take {round(time_required, 2)} seconds to extract from river."    
        
  
# Create water sources
borehole = Borehole(max_daily_extraction=10000)
river = River(flow_rate=50)  # 50 liters per second

# Requests
print(borehole.get_water(8000))       # Within limit
print(borehole.get_water(12000))      # Over limit
print(river.get_water(500))           # Calculate time   