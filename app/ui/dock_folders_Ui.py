# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dock_folders.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dock_folders(object):
    def setupUi(self, dock_folders):
        dock_folders.setObjectName("dock_folders")
        dock_folders.resize(281, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dock_folders.sizePolicy().hasHeightForWidth())
        dock_folders.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/markets"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dock_folders.setWindowIcon(icon)
        dock_folders.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        dock_folders.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        dock_folders.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ed_path = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.ed_path.setText("")
        self.ed_path.setObjectName("ed_path")
        self.verticalLayout.addWidget(self.ed_path)
        self.tree = QtWidgets.QTreeView(self.dockWidgetContents)
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)
        dock_folders.setWidget(self.dockWidgetContents)

        self.retranslateUi(dock_folders)
        QtCore.QMetaObject.connectSlotsByName(dock_folders)

    def retranslateUi(self, dock_folders):
        pass
