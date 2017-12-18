from pony.orm import *


db = Database()


class Song(db.Entity):
    Name = Required(str, 100, unique=True)
    BAnd = Optional(str, unique=True)
    data = Optional(str)
    Lyrics = Optional(str)
    Lenrth = Optional(int)
    Artits = Optional(str)
    AlbumName = Optional(str)
    Genres = Optional(str)
    artists = Set('Artists')
    playlists = Set('Playlist')
    album = Set('Album')
    idSong = PrimaryKey(int,auto=True)
    URL = Optional(str)


class Artists(db.Entity):
    Name = Required(str, unique=True)
    DataOfBirth = Optional(str)
    bands = Set('Band')
    songs = Set(Song)
    idArtist = PrimaryKey(int,auto=True)


class Band(db.Entity):
    Name = Required(str, unique=True)
    artistss = Set(Artists)
    idBand = Optional(int,auto=True)


class Playlist(db.Entity):
    Name = Required(str, unique=True)
    Description = Optional(str)
    songs = Set(Song)
    idPlaylist = Optional(int,auto=True)


class Album(db.Entity):
    name = Required(str, unique=True)
    songs = Set(Song)
    NumberofSongs = Optional(int)
    NameOfBand = Optional(str)
    idAlbum = PrimaryKey(int, auto=True)




db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

#for Song

@db_session
def addSong(name,band,Data,album,length,lyrics,artist,genres,url):
    song = Song( Name = name,
    BAnd = band,
    data = Data,
    Lyrics = lyrics,
    Lenrth = length,
    Artits = artist,
    AlbumName = album,
    Genres =genres,
    URL=url
     )
    commit()

#for Album

@db_session
def addAlbum(Name,band,numberofsong):
    album = Album( name = Name,NumberofSongs = numberofsong,
    NameOfBand = band)
    commit()

#for Artist

@db_session
def addArtist(name, Date):
    artist = Artists(Name=name, DataOfBirth=Date)
    commit()

#for Band
@db_session
def addBand(name):
    band = Band(Name=name)
    commit()

#for Playlist

@db_session
def addPlaylist(name,description):
    playlist = Playlist(Name = name,
    Description = description)
    commit()

@db_session
def s():
  Playlist.select().show()
#s()
#show(Album)

# select from database
@db_session
def selectfromPlaylist():
  playlists= select(p for p in Playlist )[:]
  return  playlists

@db_session
def selectfromsong():
  songs= select(p for p in Song )[:]
  return  songs

@db_session
def selectfromArtist():
  artists= select(p.Name for p in Artists )[:]
  return  artists

@db_session
def selectfromsAlbum():
  albums= select(p for p in Album )[:]
  return  albums

@db_session
def selectfromBand():
  bands= select(p.Name for p in Band )[:]
  return  bands

# select from database by name
@db_session
def selectfromPlaylistbyname(name):
  playlists= select(p for p in Playlist if name in p.Name )[:]

  return  playlists

@db_session
def selectfromsongbyname(name):
  songs= select(p for p in Song if name in p.Name)[:]
  return  songs

@db_session
def selectfromArtistbyname(name):
  artists= select(p for p in Artists if name in p.Name)[:]
  return  artists

@db_session
def selectfromsAlbumbyname(name):
  albums= select(p for p in Album if name in p.name )[:]
  return  albums

@db_session
def selectfromBandbyname(name):
  bands= select(p for p in Band if name in p.Name)[:]
  return  bands


@db_session
def selectfromsongbygener(gener):
  songs= select(p for p in Song if gener in p.Geners)[:]
  return  songs


@db_session
def selectfromplaylistorderbyArtist(gener):
  songs= Playlist.select(lambda p: p.price > 100).order_by(desc(Playlist.Artist))[:]
  return  songs

@db_session
def deleteplaylist(name):
   p=selectfromPlaylistbyname(name)
   for o in p:
    print(o.Name)
    if (o.Name==name):
     Playlist[o.id].delete()
     return 1


@db_session
def deletesong(name):
     p = selectfromsongbyname(name)
     for o in p:
         print(o.Name)
         if (o.Name == name):
             Song[o.idSong].delete()

@db_session
def deleteAlbum(name):
    p = selectfromsAlbumbyname(name)
    for o in p:
      print(o.name)
      if (o.name == name):
             Album[o.idAlbum].delete()

@db_session
def deleteArtist(name):
    p = selectfromArtistbyname(name)
    for o in p:
       print(o.Name)
       if (o.Name == name):
        Artists[o.idArtist].delete()

@db_session
def addsongtoplaylist(idofsong,name):
    p = selectfromPlaylistbyname(name)
    for o in p:
        #print(o.Name)
        if (o.Name == name):
           o.songs.add(Song[idofsong])
           print(o.songs.Name)

@db_session
def removesongtoplaylist(idofsong,name):
    p = selectfromPlaylistbyname(name)
    for o in p:
        #print(o.Name)
        if (o.Name == name):
           o.songs.remove(Song[idofsong])
           print(o.songs.Name)


@db_session
def showSongsinplaylist(name):
    playlist = selectfromPlaylistbyname(name)
    listofname = []
    for o in playlist:
        if (o.Name == name):
            print(o.songs.Name)
            for out in o.songs:
              listofname.append(out.Name)
    return listofname

#gga")
#deleteArtist("zz")
#for o in p :
    #l= o.songs
    #print(l.idSong)
#s()
#addsongtoplaylist(2,"zizozio")
#s()
#showSongsinplaylist("agga")
#selectfromPlaylistbyname()