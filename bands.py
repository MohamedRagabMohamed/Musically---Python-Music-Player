# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bands.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import home

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

class Ui_bands(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, bands):
        bands.setObjectName(_fromUtf8("bands"))
        bands.resize(522, 425)
        self.bandsHome = QtGui.QPushButton(bands)
        self.bandsHome.setGeometry(QtCore.QRect(150, 340, 91, 23))
        self.bandsHome.setObjectName(_fromUtf8("bandsHome"))
        self.bandsBandsNames = QtGui.QListView(bands)
        self.bandsBandsNames.setGeometry(QtCore.QRect(20, 50, 481, 251))
        self.bandsBandsNames.setObjectName(_fromUtf8("bandsBandsNames"))
        self.label_2 = QtGui.QLabel(bands)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.bandsPlaySongs = QtGui.QPushButton(bands)
        self.bandsPlaySongs.setGeometry(QtCore.QRect(30, 340, 91, 23))
        self.bandsPlaySongs.setObjectName(_fromUtf8("bandsPlaySongs"))
        self.libraryHome = QtGui.QPushButton(bands)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")

        self.retranslateUi(bands)
        QtCore.QMetaObject.connectSlotsByName(bands)

    def retranslateUi(self, bands):
        bands.setWindowTitle(_translate("bands", "\"Musicly\" Bands", None))
        self.bandsHome.setText(_translate("bands", "Home", None))
        self.label_2.setText(_translate("bands", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Bands :</span></p></body></html>", None))
        self.bandsPlaySongs.setText(_translate("bands", "Play", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.bandsPlaySongs.clicked.connect(self.openPlay)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openPlay(self):
        self