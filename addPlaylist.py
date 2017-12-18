# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPlaylist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import playlists , system.Playlist
import home , DB

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

class Ui_addPlaylist(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, addPlaylist):
        addPlaylist.setObjectName(_fromUtf8("addPlaylist"))
        addPlaylist.resize(522, 425)
        self.addPlaylistSave = QtGui.QPushButton(addPlaylist)
        self.addPlaylistSave.setGeometry(QtCore.QRect(30, 310, 75, 23))
        self.addPlaylistSave.setObjectName(_fromUtf8("addPlaylistSave"))
        self.widget = QtGui.QWidget(addPlaylist)
        self.widget.setGeometry(QtCore.QRect(20, 10, 471, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.addPlaylistName = QtGui.QLineEdit(self.widget)
        self.addPlaylistName.setObjectName(_fromUtf8("addPlaylistName"))
        self.gridLayout.addWidget(self.addPlaylistName, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.addPlaylistDescription = QtGui.QLineEdit(self.widget)
        self.addPlaylistDescription.setObjectName(_fromUtf8("addPlaylistDescription"))
        self.gridLayout.addWidget(self.addPlaylistDescription, 1, 1, 1, 1)
        self.libraryHome = QtGui.QPushButton(addPlaylist)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")

        self.retranslateUi(addPlaylist)
        QtCore.QMetaObject.connectSlotsByName(addPlaylist)

    def retranslateUi(self, addPlaylist):
        addPlaylist.setWindowTitle(_translate("addPlaylist", "\"Musicly\" AddPlaylist", None))
        self.addPlaylistSave.setText(_translate("addPlaylist", "Save", None))
        self.label_2.setText(_translate("addPlaylist", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>", None))
        self.label.setText(_translate("addPlaylist", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Description :</span></p></body></html>", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.addPlaylistSave.clicked.connect(self.openSave)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openSave(self):
        obj = system.Playlist.Playlist(self.addPlaylistName.text(),self.addPlaylistDescription.text())
        obj.addtoplaylist()
        self.libraryO = playlists.Ui_playlists()
        self.libraryO.show()
        self.hide()
