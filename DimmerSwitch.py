# DimmerSwitch class

class DimmerSwitch():
    # Inititialize switch and brightness
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    # Methods for turning the switch on and off
    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    # Methods for raising and lowering brightness
    def raiseLevel(self):
        if self.brightness < 10: # If brightness is already at 10, we don't want to be able to go higher
            self.brightness = self.brightness + 1
    
    def lowerLevel(self):
        if self.brightness > 1: # Same rule applies here as before
            self.brightness = self.brightness - 1


    # Extra method for debugging
    def show(self):
        print(f"Switch is on? {self.switchIsOn}")
        print(f'Brightness is: {self.brightness}')


# Main code
oDimmer = DimmerSwitch()

# Turn switch on and raise brightness level by 5
oDimmer.show()
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

# Turn the brightness level by 2, and turn the switch off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

# Turn switch on, and raise brightness level by 3
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()