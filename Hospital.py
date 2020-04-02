from utils import *

#A hospital class
class Hospital_TEST:
  def __init__(self, hName, hAddress, hContact, hMapLocation, hRegion, hType, hImage):
    self.hName = hName
    self.hAddress = hAddress
    self.hContact = hContact
    self.hImage = hImage
    self.hLocation = hMapLocation
    self.hNearestSubway = hRegion
    self.hType = hType
    self.hPostalCode = extractPostalCode(hAddress)

  def __str__(self):
    return "{} is located at {}\nPostal Code: {}\nNearest Subway: {}\nMapLocation: {}".format(self.hName, self.hAddress, self.hPostalCode, self.hNearestSubway, self.hLocation)


#A hospital class
class Hospital:
    def __init__(self, hName, hAddress, hContact, hLocation, hNearestSubway, hCategory, hImage, hPostCode):
        self.hName = hName
        self.hAddress = hAddress
        self.hContact = hContact
        self.hImage = hImage
        self.hLocation = hLocation
        self.hNearestSubway = hNearestSubway
        self.hCategory = hCategory
        self.hPostCode = hPostCode

class Hospital_Original:
    def __init__(self, hName, hAddress, hContact, hLocation, hNearestSubway, hCategory, hImage, hPostCode):
        self.hName = hName
        self.hAddress = hAddress
        self.hContact = hContact
        self.hImage = hImage
        self.hLocation = hLocation
        self.hNearestSubway = hNearestSubway
        self.hCategory = hCategory
        self.hPostCode = hPostCode