# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genres.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import  home ,sys
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

class Ui_genres(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, genres):
        genres.setObjectName(_fromUtf8("genres"))
        genres.resize(522, 425)
        self.genresGenreNames = QtGui.QListView(genres)
        self.genresGenreNames.setGeometry(QtCore.QRect(20, 50, 481, 251))
        self.genresGenreNames.setObjectName(_fromUtf8("genresGenreNames"))
        self.label_2 = QtGui.QLabel(genres)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.genresHome = QtGui.QPushButton(genres)
        self.genresHome.setGeometry(QtCore.QRect(150, 340, 91, 23))
        self.genresHome.setObjectName(_fromUtf8("genresHome"))
        self.genresPlaySongs = QtGui.QPushButton(genres)
        self.genresPlaySongs.setGeometry(QtCore.QRect(30, 340, 91, 23))
        self.genresPlaySongs.setObjectName(_fromUtf8("bandsPlaySongs"))
        self.libraryHome = QtGui.QPushButton(genres)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        self.retranslateUi(genres)
        QtCore.QMetaObject.connectSlotsByName(genres)

    def retranslateUi(self, genres):
        genres.setWindowTitle(_translate("genres", "\"Musicly\" Genres", None))
        self.label_2.setText(_translate("genres", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Genres :</span></p></body></html>", None))
        self.genresHome.setText(_translate("genres", "Home", None))
        self.genresPlaySongs.setText(_translate("genres", "Play", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.genresPlaySongs.clicked.connect(self.openPlay)


    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openPlay(self):
        self