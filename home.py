# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys

import playlists , artists , library , albums

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

class Ui_home(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, home):
        home.setObjectName(_fromUtf8("home"))
        home.setEnabled(True)
        home.resize(522, 425)
        self.formLayoutWidget = QtGui.QWidget(home)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 310, 501, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.formLayoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.homeArtists = QtGui.QPushButton(self.formLayoutWidget)
        self.homeArtists.setObjectName(_fromUtf8("homeArtists"))
        self.horizontalLayout_2.addWidget(self.homeArtists)
        self.homeLibrary = QtGui.QPushButton(self.formLayoutWidget)
        self.homeLibrary.setObjectName(_fromUtf8("homeLibrary"))
        self.horizontalLayout_2.addWidget(self.homeLibrary)
        self.homePlaylists = QtGui.QPushButton(self.formLayoutWidget)
        self.homePlaylists.setObjectName(_fromUtf8("homePlaylists"))
        self.horizontalLayout_2.addWidget(self.homePlaylists)
        self.homeAlbums = QtGui.QPushButton(self.formLayoutWidget)
        self.homeAlbums.setObjectName(_fromUtf8("homeAlbums"))
        self.horizontalLayout_2.addWidget(self.homeAlbums)
        self.label = QtGui.QLabel(home)
        self.label.setGeometry(QtCore.QRect(20, 70, 481, 141))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)


    def retranslateUi(self, home):
        home.setWindowTitle(_translate("home", "\"Musicly\" Home", None))
        self.homeArtists.setText(_translate("home", " Artists ", None))
        self.homeArtists.clicked.connect(self.openArtists)
        self.homeLibrary.setText(_translate("home", " Library ", None))
        self.homeLibrary.clicked.connect(self.openLibrary)
        self.homePlaylists.setText(_translate("home", " Playlists ", None))
        self.homePlaylists.clicked.connect(self.openPlaylistbtm)
        self.homeAlbums.setText(_translate("home", "Albums ", None))
        self.homeAlbums.clicked.connect(self.openAlbums)
        self.label.setText(_translate("home", "<html><head/><body><p><span style=\" font-size:28pt; color:#dd4900;\">Welcome To Musicly</span></p></body></html>", None))


    def openPlaylistbtm(self):
        self.playList = playlists.Ui_playlists()
        self.playList.show()
        self.hide()

    def openAlbums(self):
        self.album = albums.Ui_albums()
        self.album.show()
        self.hide()

    def openArtists(self):
        self.artit = artists.Ui_artists()
        self.artit.show()
        self.hide()

    def openLibrary(self):
        self.libraryO = library.Ui_library()
        self.libraryO.show()
        self.hide()


if __name__== '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_home()
    ex.show()
    sys.exit(app.exec())