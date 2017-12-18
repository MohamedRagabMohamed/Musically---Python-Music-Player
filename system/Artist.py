from DB import *

class Artist:

    def __init__(self):
        self.name=""

    def myinit(self, name,dateofbirth):
                   self.name=name
                   self.dateofbirth=dateofbirth



    def addtoArtists(self):
        addArtist(self.name,self.dateofbirth )
        #print ("Total Employee %d" )

    def showallArtist(self):
        artists = selectfromArtist()
        return artists


    def showArtist(self,name):
        artist = selectfromArtistbyname(name)
        return artist

    def deletefromArtists(self,name):
        deleteArtist(name)
#p=Artist("zzz","25/11/1996")
#p.addtoArtists()
#print(p.showArtist("zzz"))