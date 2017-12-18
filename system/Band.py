from DB import *

class Band:

    def __init__(self, name):
                   self.name=name




    def addtoBands(self):
        addBand(self.name )

    def showallband(self):
        bands = selectfromBand()
        return bands

    def showband(self,name):
        band = selectfromBandbyname(name)
        return band
            #print ("Total Employee %d"
#p=Band("z")
#p.addtoBands()
