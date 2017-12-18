# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from system.Playlist  import Playlist
from PyQt4 import QtCore, QtGui
import pygame as pg
import os , time
import home ,song , genres , bands ,DB ,system.song , viewplaylist

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

class Ui_AddSong(QtGui.QWidget):
    input = ""
    playlsitname =""
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, library):
        library.setObjectName(_fromUtf8("library"))
        library.resize(522, 425)
        self.librarySongsNames = QtGui.QListView(library)
        self.librarySongsNames.setGeometry(QtCore.QRect(25, 20, 461, 261))
        self.librarySongsNames.setObjectName(_fromUtf8("librarySongsNames"))
        self.libraryAddSong = QtGui.QPushButton(library)
        self.libraryAddSong.setGeometry(QtCore.QRect(90, 360, 81, 23))
        self.libraryAddSong.setObjectName(_fromUtf8("libraryAddSong"))

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
        library.setWindowTitle(_translate("Add Song", "\"Musicly\" Add Song", None))
        self.libraryAddSong.setText(_translate("library", "Add song", None))
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryAddSong.clicked.connect(self.openAddSong)
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openAddSong(self):
        nameofsong=self.lineEdit.text()
        nameofplaylist=self.playlsitname
        print(nameofsong+" ****** "+ nameofplaylist)
        playlist =Playlist("zzo","zz")
        playlist.addsongtoplay(nameofplaylist,nameofsong)

        self.libraryO = viewplaylist.Ui_viewPlaylist(self.playlsitname)
        self.libraryO.showsong(self.playlsitname)

        self.hide()

    def showME(self , playlistName):
        self.show()
        self.playlsitname = playlistName


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