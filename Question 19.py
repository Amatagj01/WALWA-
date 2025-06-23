"""Question 19
● Title: Abstract Class: Agricultural Sensor
● Question: Define an abstract class AgriculturalSensor with an abstract method
read_data(). Create SoilMoistureSensor and AirTemperatureSensor classes that
inherit from AgriculturalSensor and provide a concrete implementation for
read_data() which returns a simulated data reading (e.g., a random number)."""

from abc import ABC, abstractmethod
import random

# Abstract base class
class AgriculturalSensor(ABC):
    def read_data(self):
        pass

# Concrete sensor: SoilMoistureSensor
class SoilMoistureSensor(AgriculturalSensor):
    def read_data(self):
        return round(random.uniform(10.0, 60.0), 2)  # percentage moisture
   
# Concrete sensor: AirTemperatureSensor
class AirTemperatureSensor(AgriculturalSensor):
    def read_data(self):
        return round(random.uniform(20.0, 35.0), 2)  # degrees Celsius
        
        
# Create sensor objects
soil_sensor = SoilMoistureSensor()
temp_sensor = AirTemperatureSensor()

# Read and print simulated data
print("The Soil Moisture Reading is :", soil_sensor.read_data(), "%")
print("\nThe Air Temperature Reading is:", temp_sensor.read_data(), "°C")