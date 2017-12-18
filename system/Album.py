from DB import *

class Album:
    def __init__(self):
       self.name = ""
       self.numberofsong = 0

    def myinit(self, name,nameofband,numberofsong):
                   self.name=name
                   self.numberofsong=numberofsong
                   self.nameofband=nameofband



    def addtoAlbums(self):
        addAlbum(self.name,self.nameofband,self.numberofsong )
        #print ("Total Employee %d" )

    def showallAlbum(self):
        albums=selectfromsAlbum()
        return  albums

    def showAlbum(self,name):
        album=selectfromsAlbumbyname(name)
        return  album


    def deletefromAlbums(self,name):
       deleteAlbum(name)
#p=Album("zizo","mzd",21)
#p.addtoAlbums()
