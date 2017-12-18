# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlists.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import system.Playlist as ply
import viewplaylist
import addPlaylist, home

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

class Ui_playlists(QtGui.QWidget):
    input = ""
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.indx = QtCore.QModelIndex


    def setupUi(self, playlists):
        playlists.setObjectName(_fromUtf8("playlists"))
        playlists.resize(522, 425)
        self.label = QtGui.QLabel(playlists)
        self.label.setGeometry(QtCore.QRect(120, 30, 251, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.playlistsPlaylistSongs = QtGui.QListView(playlists)
        self.playlistsPlaylistSongs.setGeometry(QtCore.QRect(10, 100, 491, 181))
        #self.playlistsPlaylistSongs.resize(500,180)
        self.playlistsPlaylistSongs.setObjectName(_fromUtf8("playlistsPlaylistSongs"))
        self.label_2 = QtGui.QLabel(playlists)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.playlistsViewPlaylist = QtGui.QPushButton(playlists)
        self.playlistsViewPlaylist.setGeometry(QtCore.QRect(10, 340, 101, 23))
        self.playlistsViewPlaylist.setObjectName(_fromUtf8("playlistsViewPlaylist"))
        self.playlistsAddPlaylist = QtGui.QPushButton(playlists)
        self.playlistsAddPlaylist.setGeometry(QtCore.QRect(130, 340, 101, 23))
        self.playlistsAddPlaylist.setObjectName(_fromUtf8("playlistsAddPlaylist"))
        self.playlistsDeletePlaylist = QtGui.QPushButton(playlists)
        self.playlistsDeletePlaylist.setGeometry(QtCore.QRect(250, 340, 101, 23))
        self.playlistsDeletePlaylist.setObjectName(_fromUtf8("playlistsDeletePlaylist"))
        self.playlistsHome = QtGui.QPushButton(playlists)
        self.playlistsHome.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.playlistsHome.setObjectName(_fromUtf8("libraryHome"))
        self.playlistsHome.setStyleSheet("background-color: #E8E8E8")
        self.model = QtGui.QStandardItemModel(self.playlistsPlaylistSongs)
        self.playlistsPlaylistSongs.setWindowTitle("Playlists")
        self.showPlaylists()
        # new input methods
        self.lineEdit = QtGui.QLineEdit(playlists)
        self.lineEdit.setGeometry(QtCore.QRect(80, 300, 421, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(playlists)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 81, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(playlists)
        QtCore.QMetaObject.connectSlotsByName(playlists)

    def retranslateUi(self, playlists):
        playlists.setWindowTitle(_translate("playlists", "\"Musicly\" Playlists", None))
        self.label.setText(_translate("playlists", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5500;\">Welcome To Musicly</span></p></body></html>", None))
        self.label_2.setText(_translate("playlists", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">  Playlist :</span></p></body></html>", None))
        self.label_3.setText(_translate("playlists","<html><head/><body><p><span style=\" font-size:12pt; color:#ff5500;\">Name :</span></p></body></html>",None))
        self.playlistsViewPlaylist.setText(_translate("playlists", "View playlist", None))
        self.playlistsViewPlaylist.clicked.connect(self.openViewPlaylist)
        self.playlistsAddPlaylist.setText(_translate("playlists", "Add Playlist", None))
        self.playlistsAddPlaylist.clicked.connect(self.openAddPlaylist)
        self.playlistsHome.setText(_translate("playlists", "Back to Home", None))
        self.playlistsDeletePlaylist.setText(_translate("playlists", "Delete Playlist", None))
        self.playlistsHome.clicked.connect(self.openHome)
        self.playlistsHome.setText(_translate("library", "Home", None))
        self.playlistsDeletePlaylist.clicked.connect(self.openDeletePlaylist)



    def openHome(self):
        self.libraryO = home.Ui_home()
        self.libraryO.show()
        self.hide()

    def openViewPlaylist(self):
        self.input = self.lineEdit.text()
        self.view = viewplaylist.Ui_viewPlaylist(self.input)
        self.view.show()
        self.hide()

    def openAddPlaylist(self):
        self.add = addPlaylist.Ui_addPlaylist()
        self.add.show()
        self.hide()

    def openDeletePlaylist(self):
        self.input = self.lineEdit.text()
        ss = ply.Playlist("","")
        num = ss.deletefromplaylist(self.input)
        if(num == 1):
            #self.hide()
            self.model = QtGui.QStandardItemModel(self.playlistsPlaylistSongs)
            self.showPlaylists()
            #self.__init__()
            #self.show()

    def showPlaylists(self):
        plqy = ply.Playlist("","")
        item = QtGui.QStandardItem(" -Name                                    -Description")
        item.setCheckable(False)
        self.model.appendRow(item)
        for food in plqy.showallplaylist():
            # create an item with a caption
            string = ("-"+food.Name+"                                    -"+food.Description)
            item = QtGui.QStandardItem(string)
            # add a checkbox to it
            #item.setCheckable(True)
            # Add the item to the model
            self.model.appendRow(item)
        self.playlistsPlaylistSongs.setModel(self.model)
        self.playlistsPlaylistSongs.show()
        #self.playlistsPlaylistSongs.clicked(self.checkBoxclicked)
