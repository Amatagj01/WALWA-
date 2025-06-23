"""Question 15
● Title: Irrigation Pump Calculator
● Question: Create an IrrigationPump class with attributes pump_type and
flow_rate (in liters per minute). Add a method calculate_water_pumped() that
takes time in hours as input and returns the total volume of water pumped in"""

#Title: Irrigation Pump Calculator.
class IrrigationPump:
  def __init__(self, pump_type, flow_rate):
    self.pump_type = pump_type
    self.flow_rate = flow_rate#(in liters per minute).
    
  def calculate_water_pumped(self, hours):
        total_minutes = hours * 60
        total_water = self.flow_rate * total_minutes
        return f"The {self.pump_type} pump used for {hours} hours and pumped The total volume of {total_water} liters."
 # Ask user for pump data
pump_type = input("Enter the type of irrigation pump (e.g., Electric, Diesel, Solar,): ")
flow_rate_input = input("Enter the flow rate in liters per minute (e.g., 80): ")
hours_input = input("Enter the time the pump was used (in hours): ")  
     
#Convert strings to numbers
try:
    flow_rate = float(flow_rate_input)
    hours_used = float(hours_input)
    pump = IrrigationPump(pump_type, flow_rate)
    
    print(pump.calculate_water_pumped(hours_used))
except ValueError:
    print(" Please enter valid numeric values.") 
  
    