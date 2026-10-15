#hierarchical inheritance one parent -> multiple child
class Device:
    def power_on(self):
        print("Device switcheed on")
class Phone:
    def call(self):
        print("Making a phone call")
class computer(Device):
    def run_program(self):
        print("running a python program")
iphone=Phone()
iphone.power_on()
iphone.call()
hp=computer()
hp.power_on()
hp.run_program()
print()