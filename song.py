# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'song.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import home , playlists , addAlbum , viewplaylist , library , DB ,system.song , system.Playlist

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

class Ui_song(QtGui.QWidget):
    song_direction = ""
    name = ""
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, song):
        song.setObjectName(_fromUtf8("song"))
        song.resize(516, 436)
        self.songSaveData = QtGui.QPushButton(song)
        self.songSaveData.setGeometry(QtCore.QRect(10, 390, 75, 23))
        self.songSaveData.setObjectName(_fromUtf8("songSaveData"))
        self.layoutWidget = QtGui.QWidget(song)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 491, 331))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.songLength = QtGui.QLineEdit(self.layoutWidget)
        self.songLength.setObjectName(_fromUtf8("songLength"))
        self.gridLayout.addWidget(self.songLength, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.songBand = QtGui.QLineEdit(self.layoutWidget)
        self.songBand.setObjectName(_fromUtf8("songBand"))
        self.gridLayout.addWidget(self.songBand, 1, 2, 1, 1)
        self.songName = QtGui.QLineEdit(self.layoutWidget)
        self.songName.setObjectName(_fromUtf8("songName"))
        self.gridLayout.addWidget(self.songName, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.songArtist = QtGui.QLineEdit(self.layoutWidget)
        self.songArtist.setObjectName(_fromUtf8("songArtist"))
        self.gridLayout.addWidget(self.songArtist, 2, 2, 1, 1)
        self.songLyrics = QtGui.QLineEdit(self.layoutWidget)
        self.songLyrics.setObjectName(_fromUtf8("songLyrics"))
        self.gridLayout.addWidget(self.songLyrics, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.songGenres = QtGui.QLineEdit(self.layoutWidget)
        self.songGenres.setObjectName(_fromUtf8("songGenres"))
        self.gridLayout.addWidget(self.songGenres, 5, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.songDate = QtGui.QLineEdit(self.layoutWidget)
        self.songDate.setObjectName(_fromUtf8("songDate"))
        self.gridLayout.addWidget(self.songDate, 7, 2, 1, 1)
        self.songAlbum = QtGui.QLineEdit(self.layoutWidget)
        self.songAlbum.setObjectName(_fromUtf8("songAlbum"))
        self.gridLayout.addWidget(self.songAlbum, 6, 2, 1, 1)
        self.songFeatured = QtGui.QLineEdit(self.layoutWidget)
        self.songFeatured.setObjectName(_fromUtf8("songFeatured"))
        self.gridLayout.addWidget(self.songFeatured, 8, 2, 1, 1)
        self.songURL = QtGui.QLineEdit(song)
        self.songURL.setGeometry(QtCore.QRect(90, 360, 411, 20))
        self.songURL.setObjectName(_fromUtf8("songFeatured_3"))
        self.label_19 = QtGui.QLabel(song)
        self.label_19.setGeometry(QtCore.QRect(10, 360, 72, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))


        self.libraryHome = QtGui.QPushButton(song)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")

        self.retranslateUi(song)
        QtCore.QMetaObject.connectSlotsByName(song)

    def retranslateUi(self, song):
        song.setWindowTitle(_translate("song", "\"Musicly\" Song", None))
        self.songSaveData.setText(_translate("song", "Save", None))
        self.label_4.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Length :</span></p></body></html>", None))
        self.label_5.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Lyrics :</span></p></body></html>", None))
        self.label_2.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Band :</span></p></body></html>", None))
        self.label.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>", None))
        self.label_3.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Artist :</span></p></body></html>", None))
        self.label_6.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Genres :</span></p></body></html>", None))
        self.label_7.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Album :</span></p></body></html>", None))
        self.label_9.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Featured :</span></p></body></html>", None))
        self.label_8.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Date :</span></p></body></html>", None))
        self.label_19.setText(_translate("song", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">URL :</span></p></body></html>", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.songSaveData.clicked.connect(self.openSave)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openSave(self):
        mySong = system.song.Song()
        mySong.myinit(self.songName.text(),self.songBand.text(),self.songDate.text(),self.songAlbum.text(),int(self.songLength.text()),self.songLyrics.text(),self.songArtist.text(),self.songGenres.text(),self.songURL.text())
        mySong.addtosongs()
        #myplylist = system.Playlist.Playlist("dfghjk","dfghjkl")
        #myplylist.addsongtoplay(self.name,self.songName)
        if(self.song_direction=="addAlbum"):
            self.libraryO = addAlbum.Ui_addAlbum()
            self.libraryO.show()
            self.hide()
        elif(self.song_direction=="library"):
            self.libraryO = library.Ui_library()
            self.libraryO.show()
            self.hide()
        elif(self.song_direction=="viewplaylist"):
            self.libraryO = viewplaylist.Ui_viewPlaylist("")
            self.libraryO.show()
            self.hide()

    def showsong(self,dir):#,plylistName):
        self.song_direction = dir
        #self.name = plylistName
        self.show()