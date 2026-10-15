#encapsulation
class Phone:
    _battery="30%"
    def printbattery(self):
        print(self._battery)
iphone15=Phone()
iphone15.printbattery()