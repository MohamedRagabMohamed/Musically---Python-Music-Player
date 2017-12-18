# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAlbum.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import  sys , home , song , system.Album ,albums

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

class Ui_addAlbum(QtGui.QWidget):



    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.song_direction = ""
        self.setupUi(self)


    def setupUi(self, addAlbum):
        addAlbum.setObjectName(_fromUtf8("addAlbum"))
        addAlbum.resize(522, 425)
        self.addAlbumTitle = QtGui.QLineEdit(addAlbum)
        self.addAlbumTitle.setGeometry(QtCore.QRect(90, 10, 391, 31))
        self.addAlbumTitle.setObjectName(_fromUtf8("addAlbumTitle"))
        self.label = QtGui.QLabel(addAlbum)
        self.label.setGeometry(QtCore.QRect(20, 20, 72, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(addAlbum)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 72, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.addAlbumBandName = QtGui.QLineEdit(addAlbum)
        self.addAlbumBandName.setGeometry(QtCore.QRect(90, 50, 391, 31))
        self.addAlbumBandName.setObjectName(_fromUtf8("addAlbumBandName"))
        self.label_3 = QtGui.QLabel(addAlbum)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 141, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(addAlbum)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.addAlbumNumberOfSong = QtGui.QListView(addAlbum)
        self.addAlbumNumberOfSong.setGeometry(QtCore.QRect(160, 90, 321, 31))
        self.addAlbumNumberOfSong.setObjectName(_fromUtf8("addAlbumNumberOfSong"))
        self.addAlbumSongs = QtGui.QListView(addAlbum)
        self.addAlbumSongs.setGeometry(QtCore.QRect(110, 140, 371, 71))
        self.addAlbumSongs.setObjectName(_fromUtf8("addAlbumSongs"))
        self.addAlbumArtists = QtGui.QListView(addAlbum)
        self.addAlbumArtists.setGeometry(QtCore.QRect(110, 220, 371, 71))
        self.addAlbumArtists.setObjectName(_fromUtf8("addAlbumArtists"))
        self.label_5 = QtGui.QLabel(addAlbum)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 91, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.addAlbumSave = QtGui.QPushButton(addAlbum)
        self.addAlbumSave.setGeometry(QtCore.QRect(20, 340, 75, 23))
        self.addAlbumSave.setObjectName(_fromUtf8("addAlbumSave"))
        self.addAlbumAddSong = QtGui.QPushButton(addAlbum)
        self.addAlbumAddSong.setGeometry(QtCore.QRect(120, 340, 75, 23))
        self.addAlbumAddSong.setObjectName(_fromUtf8("addAlbumAddSong"))
        self.addAlbumAddArtist = QtGui.QPushButton(addAlbum)
        self.addAlbumAddArtist.setGeometry(QtCore.QRect(210, 340, 75, 23))
        self.addAlbumAddArtist.setObjectName(_fromUtf8("addAlbumAddArtist"))
        self.libraryHome = QtGui.QPushButton(addAlbum)
        self.libraryHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.libraryHome.setObjectName(_fromUtf8("libraryHome"))
        self.libraryHome.setStyleSheet("background-color: #E8E8E8")
        self.model = QtGui.QStandardItemModel(self.addAlbumNumberOfSong)
        self.model1 = QtGui.QStandardItemModel(self.addAlbumArtists)
        self.model2 = QtGui.QStandardItemModel(self.addAlbumSongs)
        #self.showdata()



        self.retranslateUi(addAlbum)
        QtCore.QMetaObject.connectSlotsByName(addAlbum)

    def retranslateUi(self, addAlbum):
        addAlbum.setWindowTitle(_translate("addAlbum", "\"Musicly\" addAlbum", None))
        self.label.setText(_translate("addAlbum", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Title :</span></p></body></html>", None))
        self.label_2.setText(_translate("addAlbum", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Band  :</span></p></body></html>", None))
        self.label_3.setText(_translate("addAlbum", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Number of songs :</span></p></body></html>", None))
        self.label_4.setText(_translate("addAlbum", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Song List :</span></p></body></html>", None))
        self.label_5.setText(_translate("addAlbum", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Artist List :</span></p></body></html>", None))
        self.addAlbumSave.setText(_translate("addAlbum", "Save", None))
        self.addAlbumAddSong.setText(_translate("addAlbum", "Add song", None))
        self.addAlbumAddArtist.setText(_translate("addAlbum", "Add artist", None))
        self.libraryHome.clicked.connect(self.openHome)
        self.libraryHome.setText(_translate("library", "Home", None))
        self.addAlbumSave.clicked.connect(self.openSave)
        self.addAlbumAddSong.clicked.connect(self.openAddSong)
        self.addAlbumAddArtist.clicked.connect(self.openArtist)




    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openSave(self):
        my = system.Album.Album()
        my.myinit(self.addAlbumTitle.text(),self.addAlbumBandName.text(),0)
        my.addtoAlbums()
        self.libraryO = albums.Ui_albums()
        self.libraryO.show()
        self.hide()


    def openAddSong(self):
        self.libraryO = song.Ui_song()
        self.libraryO.showsong("addAlbum")
        self.hide()

    def openArtist(self):
        self


    def showdata(self):
        plqy = system.Album.Album()
        item = QtGui.QStandardItem(plqy.numberofsong)
        item.setCheckable(False)
        self.model.appendRow(item)
        item = QtGui.QStandardItem("- Name")
        item.setCheckable(False)
        self.model.appendRow(item)
        for food in plqy.showAlbum(self.addAlbumTitle.text()):
            print(food.name)
            string = ("- " + food.name)
            item = QtGui.QStandardItem(string)
            self.model1.appendRow(item)
        self.addAlbumArtists.setModel(self.model1)
        self.addAlbumArtists.show()
        self.addAlbumNumberOfSong.setModel(self.model)
        self.addAlbumNumberOfSong.show()
        for food in plqy.showAlbum(self.addAlbumTitle.text()):
                string = ("- " + str(food.songs))
                item = QtGui.QStandardItem(string)
                self.model2.appendRow(item)
        self.addAlbumSongs.setModel(self.model2)
        self.addAlbumSongs.show()
