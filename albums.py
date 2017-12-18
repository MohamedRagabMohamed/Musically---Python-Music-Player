# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'albums.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import home , addAlbum ,system.Album ,os

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

class Ui_albums(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, albums):
        albums.setObjectName(_fromUtf8("albums"))
        albums.resize(522, 425)
        self.listView = QtGui.QListView(albums)
        self.listView.setGeometry(QtCore.QRect(20, 50, 481, 231))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_2 = QtGui.QLabel(albums)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.albumsAddNewAlbum = QtGui.QPushButton(albums)
        self.albumsAddNewAlbum.setGeometry(QtCore.QRect(20, 340, 91, 23))
        self.albumsAddNewAlbum.setObjectName(_fromUtf8("albumsAddNewAlbum"))
        self.albumsPlayAlbumSongs = QtGui.QPushButton(albums)
        self.albumsPlayAlbumSongs.setGeometry(QtCore.QRect(140, 340, 91, 23))
        self.albumsPlayAlbumSongs.setObjectName(_fromUtf8("albumsPlayAlbumSongs"))
        self.albumsDeleteAlbum = QtGui.QPushButton(albums)
        self.albumsDeleteAlbum.setGeometry(QtCore.QRect(270, 340, 91, 23))
        self.albumsDeleteAlbum.setObjectName(_fromUtf8("albumsDeleteAlbum"))
        self.libraryHome = QtGui.QPushButton(albums)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        self.model = QtGui.QStandardItemModel(self.listView)
        self.showAlbums()

        # new input methods
        self.lineEdit = QtGui.QLineEdit(albums)
        self.lineEdit.setGeometry(QtCore.QRect(80, 300, 421, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(albums)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(albums)
        QtCore.QMetaObject.connectSlotsByName(albums)

    def retranslateUi(self, albums):
        albums.setWindowTitle(_translate("albums", "\"Musicly\" Albums", None))
        self.label_2.setText(_translate("albums", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Albums :</span></p></body></html>", None))
        self.albumsAddNewAlbum.setText(_translate("albums", "Add", None))
        self.albumsPlayAlbumSongs.setText(_translate("albums", "Play", None))
        self.albumsDeleteAlbum.setText(_translate("albums", "Delete", None))
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.albumsAddNewAlbum.clicked.connect(self.openAddAlbums)
        self.albumsDeleteAlbum.clicked.connect(self.openDeleteAlbums)
        self.albumsPlayAlbumSongs.clicked.connect(self.openPlayAlbum)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openAddAlbums(self):
        self.libraryO = addAlbum.Ui_addAlbum()
        self.libraryO.show()
        self.hide()

    def openPlayAlbum(self):
        my = system.song.Song()
        songurl = my.showallsong()
        for s in songurl:
            os.startfile(s.URL)

    def openDeleteAlbums(self):
        plqy = system.Album.Album()
        plqy.deletefromAlbums(self.lineEdit.text())
        self.model = QtGui.QStandardItemModel(self.listView)
        self.showAlbums()

    def showAlbums(self):
            plqy = system.Album.Album()
            item = QtGui.QStandardItem("- Name")
            item.setCheckable(False)
            self.model.appendRow(item)
            for food in plqy.showallAlbum():
                string = ("- " + food.name)
                item = QtGui.QStandardItem(string)
                self.model.appendRow(item)
            self.listView.setModel(self.model)
            self.listView.show()