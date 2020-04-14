from utils import *

#A hospital class
class Hospital:
  def __init__(self, hName, hAddress, hContact, hMapLocation, hRegion, hType, hAbout, hImage):
    self.hName = hName
    self.hAddress = hAddress
    self.hContact = hContact
    self.hImage = hImage
    self.hLocation = hMapLocation
    self.hNearestSubway = hRegion
    self.hType = hType
    self.hAbout = hAbout
    self.hPostalCode = extractPostalCode(hAddress)

  def __str__(self):
    return "{} is located at {}\nPostal Code: {}\nNearest Subway: {}\nMapLocation: {}".format(self.hName, self.hAddress, self.hPostalCode, self.hNearestSubway, self.hLocation)
