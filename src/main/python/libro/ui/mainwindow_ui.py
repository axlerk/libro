# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\main\designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 417)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.navList = NavListWidget(self.splitter)
        self.navList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.navList.setObjectName("navList")
        self.bookTable = BookTableView(self.splitter)
        self.bookTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bookTable.setAlternatingRowColors(True)
        self.bookTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.bookTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookTable.setShowGrid(False)
        self.bookTable.setWordWrap(False)
        self.bookTable.setCornerButtonEnabled(False)
        self.bookTable.setObjectName("bookTable")
        self.bookTable.verticalHeader().setDefaultSectionSize(24)
        self.bookTable.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSend_to = QtWidgets.QMenu(self.menuFile)
        self.menuSend_to.setObjectName("menuSend_to")
        self.menuCopyToCollection = QtWidgets.QMenu(self.menuFile)
        self.menuCopyToCollection.setObjectName("menuCopyToCollection")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuCollection = QtWidgets.QMenu(self.menubar)
        self.menuCollection.setObjectName("menuCollection")
        self.menuNew = QtWidgets.QMenu(self.menuCollection)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = ToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddBooks = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/tool-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddBooks.setIcon(icon)
        self.actionAddBooks.setIconVisibleInMenu(False)
        self.actionAddBooks.setObjectName("actionAddBooks")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.actionConvertToDisk = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar/tool-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConvertToDisk.setIcon(icon1)
        self.actionConvertToDisk.setIconVisibleInMenu(False)
        self.actionConvertToDisk.setObjectName("actionConvertToDisk")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar/tool-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon2)
        self.actionSettings.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionSettings.setIconVisibleInMenu(False)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRemoveBooks = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolbar/tool-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveBooks.setIcon(icon3)
        self.actionRemoveBooks.setIconVisibleInMenu(False)
        self.actionRemoveBooks.setObjectName("actionRemoveBooks")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        self.actionAboutQt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionEditMetadata = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbar/tool-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditMetadata.setIcon(icon4)
        self.actionEditMetadata.setIconVisibleInMenu(False)
        self.actionEditMetadata.setObjectName("actionEditMetadata")
        self.actionSendToReader = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/toolbar/tool-reader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSendToReader.setIcon(icon5)
        self.actionSendToReader.setIconVisibleInMenu(False)
        self.actionSendToReader.setObjectName("actionSendToReader")
        self.actionSendBooksViaMail = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/toolbar/tool-mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSendBooksViaMail.setIcon(icon6)
        self.actionSendBooksViaMail.setIconVisibleInMenu(False)
        self.actionSendBooksViaMail.setObjectName("actionSendBooksViaMail")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSupportForum = QtWidgets.QAction(MainWindow)
        self.actionSupportForum.setObjectName("actionSupportForum")
        self.actionNewCollection = QtWidgets.QAction(MainWindow)
        self.actionNewCollection.setObjectName("actionNewCollection")
        self.actionNewSmartCollection = QtWidgets.QAction(MainWindow)
        self.actionNewSmartCollection.setObjectName("actionNewSmartCollection")
        self.actionEditCollection = QtWidgets.QAction(MainWindow)
        self.actionEditCollection.setObjectName("actionEditCollection")
        self.actionDeleteCollection = QtWidgets.QAction(MainWindow)
        self.actionDeleteCollection.setObjectName("actionDeleteCollection")
        self.actionCopyToNewCollection = QtWidgets.QAction(MainWindow)
        self.actionCopyToNewCollection.setObjectName("actionCopyToNewCollection")
        self.actionRemoveFromCollection = QtWidgets.QAction(MainWindow)
        self.actionRemoveFromCollection.setObjectName("actionRemoveFromCollection")
        self.actionAddInNewCollection = QtWidgets.QAction(MainWindow)
        self.actionAddInNewCollection.setObjectName("actionAddInNewCollection")
        self.menuSend_to.addAction(self.actionConvertToDisk)
        self.menuSend_to.addAction(self.actionSendToReader)
        self.menuSend_to.addAction(self.actionSendBooksViaMail)
        self.menuCopyToCollection.addAction(self.actionAddInNewCollection)
        self.menuFile.addAction(self.actionAddBooks)
        self.menuFile.addAction(self.actionRemoveBooks)
        self.menuFile.addAction(self.actionEditMetadata)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSend_to.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuCopyToCollection.menuAction())
        self.menuFile.addAction(self.actionRemoveFromCollection)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionSupportForum)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuNew.addAction(self.actionNewCollection)
        self.menuNew.addAction(self.actionNewSmartCollection)
        self.menuCollection.addAction(self.menuNew.menuAction())
        self.menuCollection.addAction(self.actionEditCollection)
        self.menuCollection.addAction(self.actionDeleteCollection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCollection.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionAddBooks.triggered.connect(MainWindow.onActionAddBooks)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionConvertToDisk.triggered.connect(MainWindow.onActionSendToFolder)
        self.actionSettings.triggered.connect(MainWindow.onActionSettings)
        self.actionRemoveBooks.triggered.connect(MainWindow.onActionRemoveBooks)
        self.actionAbout.triggered.connect(MainWindow.onActionAbout)
        self.actionAboutQt.triggered.connect(MainWindow.onActionAboutQt)
        self.actionEditMetadata.triggered.connect(MainWindow.onActionEditMetadata)
        self.actionSendToReader.triggered.connect(MainWindow.onActionSendToDevice)
        self.actionSendBooksViaMail.triggered.connect(MainWindow.onActionSendViaMail)
        self.actionSupportForum.triggered.connect(MainWindow.onActionSupportForum)
        self.actionHelp.triggered.connect(MainWindow.onActionHelp)
        self.actionNewCollection.triggered.connect(MainWindow.onActionNewCollection)
        self.actionNewSmartCollection.triggered.connect(MainWindow.onActionNewSmartCollection)
        self.actionEditCollection.triggered.connect(MainWindow.onActionEditCollection)
        self.actionDeleteCollection.triggered.connect(MainWindow.onActionDeleteCollection)
        self.actionAddInNewCollection.triggered.connect(MainWindow.onActionAddInNewCollection)
        self.actionRemoveFromCollection.triggered.connect(MainWindow.onActionRemoveFromCollection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSend_to.setTitle(_translate("MainWindow", "Send to..."))
        self.menuCopyToCollection.setTitle(_translate("MainWindow", "Copy to collection..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCollection.setTitle(_translate("MainWindow", "Collection"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAddBooks.setText(_translate("MainWindow", "Add"))
        self.actionAddBooks.setToolTip(_translate("MainWindow", "Add files to Libro"))
        self.actionAddBooks.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionConvertToDisk.setText(_translate("MainWindow", "Send to folder"))
        self.actionConvertToDisk.setToolTip(_translate("MainWindow", "Send files to folder"))
        self.actionSettings.setText(_translate("MainWindow", "Preferences"))
        self.actionSettings.setToolTip(_translate("MainWindow", "Libro preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionRemoveBooks.setText(_translate("MainWindow", "Remove"))
        self.actionRemoveBooks.setToolTip(_translate("MainWindow", "Remove files from Libro"))
        self.actionRemoveBooks.setShortcut(_translate("MainWindow", "Del"))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt"))
        self.actionEditMetadata.setText(_translate("MainWindow", "Edit metadata"))
        self.actionEditMetadata.setToolTip(_translate("MainWindow", "Edit files metadata"))
        self.actionSendToReader.setText(_translate("MainWindow", "Send to reader device"))
        self.actionSendToReader.setToolTip(_translate("MainWindow", "Send files to reader device"))
        self.actionSendBooksViaMail.setText(_translate("MainWindow", "Send to email"))
        self.actionSendBooksViaMail.setToolTip(_translate("MainWindow", "Send files to device email"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSupportForum.setText(_translate("MainWindow", "Support forum"))
        self.actionNewCollection.setText(_translate("MainWindow", "Collection"))
        self.actionNewCollection.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionNewSmartCollection.setText(_translate("MainWindow", "Smart collection"))
        self.actionNewSmartCollection.setShortcut(_translate("MainWindow", "Ctrl+Alt+N"))
        self.actionEditCollection.setText(_translate("MainWindow", "Edit"))
        self.actionEditCollection.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDeleteCollection.setText(_translate("MainWindow", "Delete"))
        self.actionDeleteCollection.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionCopyToNewCollection.setText(_translate("MainWindow", "New collection"))
        self.actionRemoveFromCollection.setText(_translate("MainWindow", "Remove from collection"))
        self.actionAddInNewCollection.setText(_translate("MainWindow", "New collection"))


from .booktableview import BookTableView
from .navlistwidget import NavListWidget
from .toolbar import ToolBar
from . import resources_rc
