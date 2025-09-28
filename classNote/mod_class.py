from random import choice
import random

rand_num = random.randint(1, 10)
rand_num2 = random.randint(11111111, 20111111)

name = ["tolu", "kunle", "ada", "tad", "pole", "elon", "jeff", "Marc", "James", "Kerr"]
# print(name[rand_num])
# print(choice(name))

# methods
class Vehicle:
    means_of_transportation = "Road"
    def __init__(self, name, color, model, year):
        self.name = name
        self.color = color
        self.model = model
        self.year = year
    
    def move(self):
        return(f"The {self.name} is moving")
    
    def start(self):
        return(f"The {self.name} is starting")
    
    def parking(self):
        return(f"{self.name} is parking")
    
car = Vehicle("Toyota", "Blue", "corolla", "2020",)
print(car.start())