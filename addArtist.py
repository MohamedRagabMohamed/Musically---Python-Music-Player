# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addArtist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys , home , artists , system.Artist

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

class Ui_addArtist(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, addArtist):
        addArtist.setObjectName(_fromUtf8("addArtist"))
        addArtist.resize(522, 425)
        self.addartistSave = QtGui.QPushButton(addArtist)
        self.addartistSave.setGeometry(QtCore.QRect(30, 350, 75, 23))
        self.addartistSave.setObjectName(_fromUtf8("addartistSave"))
        self.addartistName = QtGui.QLineEdit(addArtist)
        self.addartistName.setGeometry(QtCore.QRect(90, 40, 401, 20))
        self.addartistName.setObjectName(_fromUtf8("addartistName"))
        self.addartistBirthdate = QtGui.QLineEdit(addArtist)
        self.addartistBirthdate.setGeometry(QtCore.QRect(112, 90, 381, 20))
        self.addartistBirthdate.setObjectName(_fromUtf8("addartistBirthdate"))
        self.label = QtGui.QLabel(addArtist)
        self.label.setGeometry(QtCore.QRect(30, 40, 72, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(addArtist)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 72, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.libraryHome = QtGui.QPushButton(addArtist)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")

        self.retranslateUi(addArtist)
        QtCore.QMetaObject.connectSlotsByName(addArtist)

    def retranslateUi(self, addArtist):
        addArtist.setWindowTitle(_translate("addArtist", "\"Musicly\" AddArtist", None))
        self.addartistSave.setText(_translate("addArtist", "Save", None))
        self.label.setText(_translate("addArtist", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>", None))
        self.label_2.setText(_translate("addArtist", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Birthdate :</span></p></body></html>", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.addartistSave.clicked.connect(self.openSave)

    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openSave(self):
        ply = system.Artist.Artist()
        ply.myinit(self.addartistName.text(),self.addartistBirthdate.text())
        ply.addtoArtists()
        self.libraryO = artists.Ui_artists()
        self.libraryO.show()
        self.hide()
