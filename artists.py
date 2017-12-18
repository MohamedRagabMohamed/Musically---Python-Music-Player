# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'artists.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import  home , addArtist ,system.Artist ,os

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

class Ui_artists(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, artists):
        artists.setObjectName(_fromUtf8("artists"))
        artists.resize(522, 425)
        #color start
        pal = QtGui.QPalette()
        col =  QtGui.QColor
        #pal.setColor(QtGui.QPalette.Active,col)


        #color end
        self.artistsNames = QtGui.QListView(artists)
        self.artistsNames.setGeometry(QtCore.QRect(10, 60, 491, 230))
        self.artistsNames.setObjectName(_fromUtf8("artistsNames"))
        self.artistsAddNewArtist = QtGui.QPushButton(artists)
        self.artistsAddNewArtist.setGeometry(QtCore.QRect(20, 350, 91, 23))
        self.artistsAddNewArtist.setObjectName(_fromUtf8("artistsAddNewArtist"))
        self.artistsDeleteArtist = QtGui.QPushButton(artists)
        self.artistsDeleteArtist.setGeometry(QtCore.QRect(150, 350, 91, 23))
        self.artistsDeleteArtist.setObjectName(_fromUtf8("artistsDeleteArtist"))
        self.artistsPlayArtistSongs = QtGui.QPushButton(artists)
        self.artistsPlayArtistSongs.setGeometry(QtCore.QRect(280, 350, 91, 23))
        self.artistsPlayArtistSongs.setObjectName(_fromUtf8("artistsPlayArtistSongs"))
        self.libraryHome = QtGui.QPushButton(artists)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        self.model = QtGui.QStandardItemModel(self.artistsNames)
        self.showArtist()

        # new input methods
        self.lineEdit = QtGui.QLineEdit(artists)
        self.lineEdit.setGeometry(QtCore.QRect(80, 300, 421, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(artists)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))


        self.retranslateUi(artists)
        QtCore.QMetaObject.connectSlotsByName(artists)

    def retranslateUi(self, artists):
        artists.setWindowTitle(_translate("artists", "\"Musicly\" Artists", None))
        self.artistsAddNewArtist.setText(_translate("artists", "Add", None))
        self.artistsDeleteArtist.setText(_translate("artists", "Delete", None))
        self.artistsPlayArtistSongs.setText(_translate("artists", "Play", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.artistsAddNewArtist.clicked.connect(self.openAdd)
        self.artistsDeleteArtist.clicked.connect(self.openDelete)
        self.artistsPlayArtistSongs.clicked.connect(self.openPlay)
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))


    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openAdd(self):
        self.libraryO = addArtist.Ui_addArtist()
        self.libraryO.show()
        self.hide()

    def openDelete(self):
        plqy = system.Artist.Artist()
        plqy.deletefromArtists(self.lineEdit.text())
        self.model = QtGui.QStandardItemModel(self.artistsNames)
        self.showArtist()

    def openPlay(self):
        my = system.song.Song()
        songurl = my.showallsong()
        for s in songurl:
            os.startfile(s.URL)


    def showArtist(self):
        plqy = system.Artist.Artist()
        item = QtGui.QStandardItem("- Name")
        item.setCheckable(False)
        self.model.appendRow(item)
        for food in plqy.showallArtist():
            string = ("- " + food)
            item = QtGui.QStandardItem(string)
            self.model.appendRow(item)
        self.artistsNames.setModel(self.model)
        self.artistsNames.show()