"""Question 18
● Title: Abstract Class: Farm Task
● Question: Create an abstract base class FarmTask using the abc module, with an
abstract method execute(). Create two concrete classes, PloughingTask and
SowingTask, that inherit from FarmTask and implement the execute() method with
a print statement describing the action (e.g., "Executing ploughing on Field A")."""

# Title: Abstract Class: Farm Task
from abc import ABC, abstractmethod

# Abstract base class
class FarmTask(ABC):
    def execute(self):
        pass

# Concrete subclass: PloughingTask
class PloughingTask(FarmTask):
    def execute(self):
        print("Executing ploughing on Field A.")

# Concrete subclass: SowingTask
class SowingTask(FarmTask):
    def execute(self):
        print("Executing sowing of maize on Field B.")
        
# Instantiate and execute tasks
task1 = PloughingTask()
task2 = SowingTask()

task1.execute()
task2.execute()