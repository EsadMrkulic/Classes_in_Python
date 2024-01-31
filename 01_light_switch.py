'''
Same code from 00_light_switch.py
However, this time we're using multiple objects
'''

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
oLightSwitch1 = LightSwitch() # Creating a Light Switch object
oLightSwitch2 = LightSwitch() # Creating another Light Switch object

# Test code
oLightSwitch1.show()
oLightSwitch2.show()

oLightSwitch1.TurnOn() # Turn LightSwitch1 on

# LightSwitch2 should already be off, but we do this to show that it does not affect LS1 as they are separate objects
oLightSwitch2.TurnOff() 
oLightSwitch1.show()
oLightSwitch2.show()

# Results should be
# LS1 off
# LS2 off
# LS1 on
# LS2 off