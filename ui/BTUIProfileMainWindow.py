# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/BTUIProfileMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileMainWindow(object):
    def setupUi(self, ProfileMainWindow):
        ProfileMainWindow.setObjectName("ProfileMainWindow")
        ProfileMainWindow.resize(302, 343)
        self.centralwidget = QtWidgets.QWidget(ProfileMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listProfiles = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("CMU Serif")
        font.setPointSize(12)
        self.listProfiles.setFont(font)
        self.listProfiles.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listProfiles.setAcceptDrops(True)
        self.listProfiles.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listProfiles.setDragEnabled(True)
        self.listProfiles.setDragDropOverwriteMode(True)
        self.listProfiles.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listProfiles.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listProfiles.setObjectName("listProfiles")
        self.verticalLayout.addWidget(self.listProfiles)
        self.buttonShowTOTP = QtWidgets.QPushButton(self.centralwidget)
        self.buttonShowTOTP.setObjectName("buttonShowTOTP")
        self.verticalLayout.addWidget(self.buttonShowTOTP)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        ProfileMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProfileMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 22))
        self.menubar.setObjectName("menubar")
        self.menuProfiles = QtWidgets.QMenu(self.menubar)
        self.menuProfiles.setObjectName("menuProfiles")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        ProfileMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProfileMainWindow)
        self.statusbar.setObjectName("statusbar")
        ProfileMainWindow.setStatusBar(self.statusbar)
        self.actionRenameAccount = QtWidgets.QAction(ProfileMainWindow)
        self.actionRenameAccount.setObjectName("actionRenameAccount")
        self.actionAddAccount = QtWidgets.QAction(ProfileMainWindow)
        self.actionAddAccount.setObjectName("actionAddAccount")
        self.actionDeleteAccount = QtWidgets.QAction(ProfileMainWindow)
        self.actionDeleteAccount.setObjectName("actionDeleteAccount")
        self.actionCopy2Clipboard = QtWidgets.QAction(ProfileMainWindow)
        self.actionCopy2Clipboard.setCheckable(True)
        self.actionCopy2Clipboard.setChecked(True)
        self.actionCopy2Clipboard.setObjectName("actionCopy2Clipboard")
        self.actionExit = QtWidgets.QAction(ProfileMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAutoTOTPHide = QtWidgets.QAction(ProfileMainWindow)
        self.actionAutoTOTPHide.setCheckable(True)
        self.actionAutoTOTPHide.setChecked(True)
        self.actionAutoTOTPHide.setObjectName("actionAutoTOTPHide")
        self.actionOpenProfile = QtWidgets.QAction(ProfileMainWindow)
        self.actionOpenProfile.setObjectName("actionOpenProfile")
        self.actionChangeProfile = QtWidgets.QAction(ProfileMainWindow)
        self.actionChangeProfile.setObjectName("actionChangeProfile")
        self.actionSave = QtWidgets.QAction(ProfileMainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionChangePassword = QtWidgets.QAction(ProfileMainWindow)
        self.actionChangePassword.setObjectName("actionChangePassword")
        self.menuProfiles.addAction(self.actionChangeProfile)
        self.menuProfiles.addSeparator()
        self.menuProfiles.addAction(self.actionSave)
        self.menuProfiles.addSeparator()
        self.menuProfiles.addAction(self.actionRenameAccount)
        self.menuProfiles.addAction(self.actionAddAccount)
        self.menuProfiles.addAction(self.actionDeleteAccount)
        self.menuProfiles.addSeparator()
        self.menuProfiles.addAction(self.actionChangePassword)
        self.menuProfiles.addSeparator()
        self.menuProfiles.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionCopy2Clipboard)
        self.menuOptions.addAction(self.actionAutoTOTPHide)
        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(ProfileMainWindow)
        self.closeButton.clicked.connect(ProfileMainWindow.close)
        self.actionExit.triggered.connect(ProfileMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ProfileMainWindow)

    def retranslateUi(self, ProfileMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileMainWindow.setWindowTitle(_translate("ProfileMainWindow", "MainWindow"))
        self.buttonShowTOTP.setText(_translate("ProfileMainWindow", "Show TOTP"))
        self.closeButton.setText(_translate("ProfileMainWindow", "Close"))
        self.menuProfiles.setTitle(_translate("ProfileMainWindow", "Profile"))
        self.menuOptions.setTitle(_translate("ProfileMainWindow", "Options"))
        self.actionRenameAccount.setText(_translate("ProfileMainWindow", "Rename Account"))
        self.actionAddAccount.setText(_translate("ProfileMainWindow", "New Account"))
        self.actionAddAccount.setToolTip(_translate("ProfileMainWindow", "New Account"))
        self.actionDeleteAccount.setText(_translate("ProfileMainWindow", "Delete Account"))
        self.actionDeleteAccount.setToolTip(_translate("ProfileMainWindow", "Delete Account"))
        self.actionCopy2Clipboard.setText(_translate("ProfileMainWindow", "Copy to Clipboard"))
        self.actionExit.setText(_translate("ProfileMainWindow", "Exit"))
        self.actionAutoTOTPHide.setText(_translate("ProfileMainWindow", "Hide TOTP Automatically"))
        self.actionOpenProfile.setText(_translate("ProfileMainWindow", "Open Profile"))
        self.actionChangeProfile.setText(_translate("ProfileMainWindow", "Change Profile"))
        self.actionSave.setText(_translate("ProfileMainWindow", "Save (Ctrl+S)"))
        self.actionChangePassword.setText(_translate("ProfileMainWindow", "Change Password"))
