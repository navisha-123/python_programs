#inheritance
#single innheritance - one parent class adn one child class

class Device:
    def power_on(self):
        print("Device switched on")
class Phone(Device):
    def call(self):
        print("making a phone call")
samsung=Phone()
samsung.call()
samsung.power_on()