from DB import *

class Playlist:

    def __init__(self, name,discription):
                   self.name=name
                   self.discription=discription



    def addtoplaylist(self):
        addPlaylist(self.name,self.discription )
        #print ("Total Employee %d" )

#p=Playlist("zizomoy","zzz")
#p.addtoplaylist()

    def showallplaylist(self):
        playlists=selectfromPlaylist()
        return  playlists

    def showplaylistbyname(self,name):
        playlist=selectfromPlaylistbyname(name)
        return  playlist

    def showSongs(self, name):

        return showSongsinplaylist(name)

    def deletefromplaylist(self,name):
        return deleteplaylist(name)



    def addsongtoplay(self, nameofplaylist,nameofsong):
        p=selectfromPlaylistbyname(nameofplaylist)
        for i in p:
            print(i.Name)
            if (i.Name==nameofplaylist):
                s=selectfromsongbyname(nameofsong)
                for j in s:
                   print(j.Name)
                   if (j.Name==nameofsong):
                    addsongtoplaylist(j.idSong,nameofplaylist)


    def removesongtoplay(self, nameofplaylist,nameofsong):
        p=selectfromPlaylistbyname(nameofplaylist)
        for i in p:
            if (i.Name==nameofplaylist):
                s=selectfromsongbyname(nameofsong)
                for j in s:
                   if (j.Name==nameofsong):
                    removesongtoplaylist(j.idSong,nameofplaylist)

#p=Playlist("zizoionnnnjjjmmmmm","zzz")
#p.addtoplaylist()

#p.removesongtoplay("zizoionnnnjjjmmmmm","name")