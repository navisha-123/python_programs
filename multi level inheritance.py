# #multilevel inheritance grandparent class -> parent claass -> child class

class Device:
    def power_one(self):
        print("DEvice switched on")
class computer:
    def run_program(self):
        print("Running a python program")
class laptop(computer):
    def charge(self):
        print("Laptop battery charging")

asus=laptop()
asus.power_on()
asus.run_program()
asus.charge()
print()

