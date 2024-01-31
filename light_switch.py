from time import sleep

# Classes with light switches


# Light switch class
class LightSwitch():
    # Initialization first
    def __init__(self):
        # Inititialize a variable with self, and set it to False as its start
        self.switchIsOn = False

    # Method to turn the switch on
    def TurnOn(self):
        self.switchIsOn = True

    # Method to turn the switch off
    def TurnOff(self):
        self.switchIsOn = False

    def show(self): # Added for testing purposes
        sleep(1)
        if self.switchIsOn == True:
            print('The switch is on')
        else:
            print('The switch is off')


# Main code

# Creating a switch object
oLightSwitch = LightSwitch()

# Calling the methods
oLightSwitch.show()
oLightSwitch.TurnOn()
oLightSwitch.show()
oLightSwitch.TurnOff()
oLightSwitch.show()