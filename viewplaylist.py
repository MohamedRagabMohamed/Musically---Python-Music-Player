# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewplaylist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pony.orm import  *
import home , system.Playlist , addSong
import song ,DB ,os , time , playlists
from system.Playlist  import Playlist


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_viewPlaylist(QtGui.QWidget):
    input = ""
    playlistname = ""
    def __init__(self,name):
        self.input = name
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, viewPlaylist):
        viewPlaylist.setObjectName(_fromUtf8("viewPlaylist"))
        viewPlaylist.resize(522, 425)
        self.viewPlaylistSongs = QtGui.QListView(viewPlaylist)
        self.viewPlaylistSongs.setGeometry(QtCore.QRect(20, 160, 481, 131))
        self.viewPlaylistSongs.setObjectName(_fromUtf8("viewPlaylistSongs"))
        self.viewPlaylistName = QtGui.QListView(viewPlaylist)
        self.viewPlaylistName.setGeometry(QtCore.QRect(20, 60, 481, 31))
        self.viewPlaylistName.setObjectName(_fromUtf8("viewPlaylistName"))
        self.viewPlaylistDescription = QtGui.QListView(viewPlaylist)
        self.viewPlaylistDescription.setGeometry(QtCore.QRect(20, 110, 481, 31))
        self.viewPlaylistDescription.setObjectName(_fromUtf8("viewPlaylistDescription"))
        self.viewPlaylistDeletePlaylist = QtGui.QPushButton(viewPlaylist)
        self.viewPlaylistDeletePlaylist.setGeometry(QtCore.QRect(20, 360, 91, 23))
        self.viewPlaylistDeletePlaylist.setObjectName(_fromUtf8("viewPlaylistDeletePlaylist"))
        self.viewPlaylistPlaySongs = QtGui.QPushButton(viewPlaylist)
        self.viewPlaylistPlaySongs.setGeometry(QtCore.QRect(150, 360, 91, 23))
        self.viewPlaylistPlaySongs.setObjectName(_fromUtf8("viewPlaylistPlaySongs"))
        self.viewPlaylistAddSongToPlaylist = QtGui.QPushButton(viewPlaylist)
        self.viewPlaylistAddSongToPlaylist.setGeometry(QtCore.QRect(280, 360, 91, 23))
        self.viewPlaylistAddSongToPlaylist.setObjectName(_fromUtf8("viewPlaylistAddSongToPlaylist"))
        self.viewPlaylistRemoveSongeFromPlaylist = QtGui.QPushButton(viewPlaylist)
        self.viewPlaylistRemoveSongeFromPlaylist.setGeometry(QtCore.QRect(410, 360, 91, 23))
        self.viewPlaylistRemoveSongeFromPlaylist.setObjectName(_fromUtf8("viewPlaylistRemoveSongeFromPlaylist"))
        self.libraryHome = QtGui.QPushButton(viewPlaylist)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        # new input methods
        self.lineEdit = QtGui.QLineEdit(viewPlaylist)
        self.lineEdit.setGeometry(QtCore.QRect(80, 300, 421, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(viewPlaylist)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.model = QtGui.QStandardItemModel(self.viewPlaylistName)
        self.model1 = QtGui.QStandardItemModel(self.viewPlaylistDescription)
        self.model2 = QtGui.QStandardItemModel(self.viewPlaylistSongs)
        self.showData()



        self.retranslateUi(viewPlaylist)
        QtCore.QMetaObject.connectSlotsByName(viewPlaylist)

    def retranslateUi(self, viewPlaylist):
        viewPlaylist.setWindowTitle(_translate("viewPlaylist", "\"Musicly\" ViewPlaylist", None))
        self.viewPlaylistDeletePlaylist.setText(_translate("viewPlaylist", "Delete", None))
        self.viewPlaylistPlaySongs.setText(_translate("viewPlaylist", "Play", None))
        self.viewPlaylistAddSongToPlaylist.setText(_translate("viewPlaylist", "Add song", None))
        self.viewPlaylistRemoveSongeFromPlaylist.setText(_translate("viewPlaylist", "Remove song", None))
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.viewPlaylistAddSongToPlaylist.clicked.connect(self.openAddSong)
        self.viewPlaylistPlaySongs.clicked.connect(self.openPlay)
        self.viewPlaylistDeletePlaylist.clicked.connect(self.openDelete)
        self.viewPlaylistRemoveSongeFromPlaylist.clicked.connect(self.openRemove)


    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openAddSong(self):
        self.libraryO = addSong.Ui_AddSong()
        self.libraryO.showME(self.input)
        self.hide()

    def openPlay(self):
        my = system.song.Song()
        songurl = my.showallsong()
        for s in songurl:
            os.startfile(s.URL)
            time.sleep(10)

    def openDelete(self):
        playlist = Playlist(self.playlistname, "zz")
        playlist.deletefromplaylist(self.playlistname)
        self.libraryO = playlists.Ui_playlists()
        self.libraryO.show()
        self.hide()

    def openRemove(self):
        nameofsong = self.lineEdit.text()
        nameofplaylist = self.playlistname
        print(nameofsong + " ****** " + nameofplaylist)
        playlist = Playlist("zzo", "zz")
        playlist.removesongtoplay(nameofplaylist, nameofsong)

        self.hide()
        self.model.clear()
        self.model1.clear()
        self.model2.clear()
        self.show()
        self.showData()


    def setInput(self,name):
        self.input=name
    def showData(self):
        tem = system.Playlist.Playlist("a7a","a7a")
        for food in tem.showplaylistbyname(self.input):
            print(type(food.Name), "777")
            self.playlistname= food.Name
            item = QtGui.QStandardItem(food.Name)
            self.model.appendRow(item)
            self.viewPlaylistName.setModel(self.model)
            self.viewPlaylistName.show()
            print(type(food.Description), "777")
            item = QtGui.QStandardItem(food.Description)
            self.model1.appendRow(item)
            self.viewPlaylistDescription.setModel(self.model1)
            self.viewPlaylistDescription.show()
            #print(type(food.songs))
            for dat in tem.showSongs(self.input):
                item = QtGui.QStandardItem(dat)
                self.model2.appendRow(item)
                self.viewPlaylistSongs.setModel(self.model2)
                self.viewPlaylistSongs.show()

    def showsong(self , name):
        self.show()
        self.input = name
        #self.showData()