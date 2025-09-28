# import mod_class as mc
import mod_class as mc

car = mc.Vehicle("toyota", "blue", "corolla", "2020")
# print(car.name)

class landVehicle(mc.Vehicle):
    def __init__(self, name, color, model, year, wheel):
        super().__init__(name, color, model, year)
        self.wheel = wheel

    def reverse(self):
        return f"The {self.name} is reversing"
    
car = landVehicle("toyota", "green", "corolla", "2025", 5)
print(car.reverse())
