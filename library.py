# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pygame as pg
import os , time
import home ,song , genres , bands ,DB ,system.song

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

class Ui_library(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, library):
        library.setObjectName(_fromUtf8("library"))
        library.resize(522, 425)
        self.librarySongsNames = QtGui.QListView(library)
        self.librarySongsNames.setGeometry(QtCore.QRect(25, 20, 461, 261))
        self.librarySongsNames.setObjectName(_fromUtf8("librarySongsNames"))
        self.libraryPlayGenre = QtGui.QPushButton(library)
        self.libraryPlayGenre.setGeometry(QtCore.QRect(250, 360, 81, 23))
        self.libraryPlayGenre.setObjectName(_fromUtf8("libraryPlayGenre"))
        self.libraryAddSong = QtGui.QPushButton(library)
        self.libraryAddSong.setGeometry(QtCore.QRect(90, 360, 81, 23))
        self.libraryAddSong.setObjectName(_fromUtf8("libraryAddSong"))
        self.libraryDeleteSong = QtGui.QPushButton(library)
        self.libraryDeleteSong.setGeometry(QtCore.QRect(170, 360, 81, 23))
        self.libraryDeleteSong.setObjectName(_fromUtf8("libraryDeleteSong"))
        self.libraryPlayAll = QtGui.QPushButton(library)
        self.libraryPlayAll.setGeometry(QtCore.QRect(410, 360, 81, 23))
        self.libraryPlayAll.setObjectName(_fromUtf8("libraryPlayAll"))
        self.libraryPlayBand = QtGui.QPushButton(library)
        self.libraryPlayBand.setGeometry(QtCore.QRect(330, 360, 81, 23))
        self.libraryPlayBand.setObjectName(_fromUtf8("libraryPlayBand"))
        self.libraryPlaySong = QtGui.QPushButton(library)
        self.libraryPlaySong.setGeometry(QtCore.QRect(10, 360, 81, 23))
        self.libraryPlaySong.setObjectName(_fromUtf8("libraryPlaySong"))
        self.libraryHome = QtGui.QPushButton(library)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        self.model = QtGui.QStandardItemModel(self.librarySongsNames)
        self.showSongS()

        # new input methods
        self.lineEdit = QtGui.QLineEdit(library)
        self.lineEdit.setGeometry(QtCore.QRect(69, 300, 421, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(library)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))



        self.retranslateUi(library)
        QtCore.QMetaObject.connectSlotsByName(library)

    def retranslateUi(self, library):
        library.setWindowTitle(_translate("library", "\"Musicly\" library", None))
        self.libraryPlayGenre.setText(_translate("library", "Play genre", None))
        self.libraryAddSong.setText(_translate("library", "Add song", None))
        self.libraryDeleteSong.setText(_translate("library", "Delete song", None))
        self.libraryPlayAll.setText(_translate("library", "Play all", None))
        self.libraryPlayBand.setText(_translate("library", "Play band", None))
        self.libraryPlaySong.setText(_translate("library", "Play song", None))
        self.libraryHome.setText(_translate("library","Home",None))
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryAddSong.clicked.connect(self.openAddSong)
        self.libraryPlaySong.clicked.connect(self.openPlaySong)
        self.libraryDeleteSong.clicked.connect(self.openDeleteSong)
        self.libraryPlayGenre.clicked.connect(self.openPlayGenre)
        self.libraryPlayBand.clicked.connect(self.openPlayBand)
        self.libraryPlayAll.clicked.connect(self.openPlayAllSongs)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openAddSong(self):
        print("a7aaaaaaaaaaa")
        self.libraryO = song.Ui_song()
        self.libraryO.showsong("library")
        self.hide()

    def openPlaySong(self):
        my = system.song.Song()
        songurl = my.showsongbyname(self.lineEdit.text())
        for s in songurl:
            os.startfile(s.URL)

    def openDeleteSong(self):
        my = system.song.Song()
        songurl = my.deletefromsongs(self.lineEdit.text())
        self.model = QtGui.QStandardItemModel(self.librarySongsNames)
        self.showSongS()

    def showSongS(self):
        plqy = system.song.Song()
        item = QtGui.QStandardItem("- Name")
        item.setCheckable(False)
        self.model.appendRow(item)
        for food in plqy.showallsong():
            string = ("- " + food.Name)
            item = QtGui.QStandardItem(string)
            self.model.appendRow(item)
        self.librarySongsNames.setModel(self.model)
        self.librarySongsNames.show()

    def openPlayGenre(self):
        self.libraryO = genres.Ui_genres()
        self.hide()
        self.libraryO.show()



    def openPlayBand(self):
        self.libraryO = bands.Ui_bands()
        self.hide()
        self.libraryO.show()


    def openPlayAllSongs(self):
        my = system.song.Song()
        songurl = my.showallsong()
        for s in songurl:
            os.startfile(s.URL)
            time.sleep(10)