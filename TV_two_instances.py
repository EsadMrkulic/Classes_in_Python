# TV Class
class TV():
    # Inizialize variables
    def __init__(self):
        self.isOn = False
        self.isMuted = False
         
        # A defualt list of channels 
        self.channelList = [2, 4, 7, 10, 11, 14, 17, 18, 19, 22, 29, 30, 37, 47, 55, 57]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0

        # Volumes are constant
        self.VOLUME_MIN = 0 
        self.VOLUME_MAX = 10
        
        # Set the volume to half the max everytime a new TV is created
        # Use floor division rather than regular division to not get decimals
        self.volume = self.VOLUME_MAX // 2 # Even though 10/2 = 5, it's still good practice to use floor division for a case like a TV volume

    #Function to turn TV off and on
    def power(self):
        self.isOn = not self.isOn

    # Increase volume function
    def volumeUp(self):
        # First, check to see if TV is on
        if self.isOn == False:
            return
        
        # If TV is muted, clicking the volume up button turns the TV on
        if self.isMuted == True:
            self.isMuted = False

        if self.volume < self.VOLUME_MAX:
            self.volume = self.volume + 1

    # Decrease volume function
    def volumeDown(self):
        # First, check to see if TV is on
        if self.isOn == False:
            return
        
        # If TV is muted, clicking the volume down button turns the TV on
        if self.isMuted == True:
            self.isMuted = False

        if self.volume > self.VOLUME_MIN:
            self.volume = self.volume - 1

    # Changing channel up function
    def channelUp(self):
        # First, check to see if TV is on
        if not self.isOn:
            return
        
        # Increase the channel by 1
        self.channelIndex = self.channelIndex + 1

        # If the channel number exceeds the highest channel number, wrap back around to the first channel
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    # Changing channel down function
    def channelDown(self):
        # First, check to see if TV is on
        if not self.isOn:
            return
        
        # Decrease the channel by 1
        self.channelIndex = self.channelIndex - 1

        # If the channel number is less than lowest channel number, wrap back around to the top channel
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    
    # Mute function
    def mute(self):
        # First check if TV is on
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    #Function to set channel by number
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
            # If the new channel is not in the list, do nothing 

    # Function for testing
    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('    TV is: On')
            print('    Channel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is: ', self.volume, ' (sound is muted)')
            else:
                print('    Volume is:', self.volume)

        else:
            print('    TV is off')


# Main code
# 2 TV Instances
oTV1 = TV() # Create 1 TV Object
oTV2 = TV() # Create a second TV Object

# Turn both TV's on
oTV1.power()
oTV2.power()

# Raise the volume of TV 1
oTV1.volumeUp()
oTV1.volumeUp()

# Raise the volume of TV 2
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

#Change TV 2's channel then mute it
oTV2.setChannel(22)
oTV2.mute()

# Show the info for both TV's
oTV1.showInfo()
oTV2.showInfo()
