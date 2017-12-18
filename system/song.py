from DB import *

class Song:
    def __init__(self):
        self.name = ""

    def myinit(self, name,band,Data,album,length,lyrics,artist,genres,url):
                   self.name=name
                   self.band=band
                   self.Data=Data
                   self.lyrics=lyrics
                   self.length=length
                   self.artist=artist
                   self.album=album
                   self.genres=genres
                   self.url=url


    def addtosongs(self):
        addSong(self.name,self.band,self.Data,self.album,self.length,self.lyrics,self.artist,self.genres,self.url )
        print ("Total Employee %d" )

    def showallsong(self):
        songs=selectfromsong()
        return  songs

    def showsongbyname(self,name):
        songs = selectfromsongbyname(name)
        return songs

    def deletefromsongs(self, name):
        deletesong(name)

#s=Song("namezzzzmmbbb","bandmmjmmmjjj","Data","album",20,"lyrics","artist","genres","yrl")
#s.addtosongs()