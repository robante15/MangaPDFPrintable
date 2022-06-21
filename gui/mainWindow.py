# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_inputFolder = QtWidgets.QLabel(self.groupBox)
        self.lbl_inputFolder.setObjectName("lbl_inputFolder")
        self.horizontalLayout.addWidget(self.lbl_inputFolder)
        self.txt_inputFolder = QtWidgets.QLineEdit(self.groupBox)
        self.txt_inputFolder.setObjectName("txt_inputFolder")
        self.horizontalLayout.addWidget(self.txt_inputFolder)
        self.btn_openFolder = QtWidgets.QPushButton(self.groupBox)
        self.btn_openFolder.setObjectName("btn_openFolder")
        self.horizontalLayout.addWidget(self.btn_openFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_sortOrder = QtWidgets.QLabel(self.groupBox)
        self.lbl_sortOrder.setObjectName("lbl_sortOrder")
        self.horizontalLayout_5.addWidget(self.lbl_sortOrder)
        self.rbtn_sortName = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn_sortName.setChecked(True)
        self.rbtn_sortName.setObjectName("rbtn_sortName")
        self.horizontalLayout_5.addWidget(self.rbtn_sortName)
        self.rbtn_sortCreationDate = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn_sortCreationDate.setObjectName("rbtn_sortCreationDate")
        self.horizontalLayout_5.addWidget(self.rbtn_sortCreationDate)
        self.sort_includeSubfolder = QtWidgets.QCheckBox(self.groupBox)
        self.sort_includeSubfolder.setObjectName("sort_includeSubfolder")
        self.horizontalLayout_5.addWidget(self.sort_includeSubfolder)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_loadFolderFiles = QtWidgets.QPushButton(self.groupBox)
        self.btn_loadFolderFiles.setObjectName("btn_loadFolderFiles")
        self.horizontalLayout_6.addWidget(self.btn_loadFolderFiles)
        self.btn_ShowPicture = QtWidgets.QPushButton(self.groupBox)
        self.btn_ShowPicture.setObjectName("btn_ShowPicture")
        self.horizontalLayout_6.addWidget(self.btn_ShowPicture)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.btn_sortTableRise = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sortTableRise.setObjectName("btn_sortTableRise")
        self.verticalLayout_3.addWidget(self.btn_sortTableRise)
        self.btn_sortTableAddSeparator = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sortTableAddSeparator.setObjectName("btn_sortTableAddSeparator")
        self.verticalLayout_3.addWidget(self.btn_sortTableAddSeparator)
        self.btn_sortTableDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sortTableDelete.setObjectName("btn_sortTableDelete")
        self.verticalLayout_3.addWidget(self.btn_sortTableDelete)
        self.btn_sortTableDescend = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sortTableDescend.setObjectName("btn_sortTableDescend")
        self.verticalLayout_3.addWidget(self.btn_sortTableDescend)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.table_filesList = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_filesList.setObjectName("table_filesList")
        self.table_filesList.setColumnCount(1)
        self.table_filesList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_filesList.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_2.addWidget(self.table_filesList)
        self.gfx_Preview = QtWidgets.QGraphicsView(self.groupBox_2)
        self.gfx_Preview.setObjectName("gfx_Preview")
        self.horizontalLayout_2.addWidget(self.gfx_Preview)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.lbl_inputFolder.setText(_translate("MainWindow", "Directorio de Entrada"))
        self.btn_openFolder.setText(_translate("MainWindow", "Seleccionar"))
        self.lbl_sortOrder.setText(_translate("MainWindow", "Orden de Importación:"))
        self.rbtn_sortName.setText(_translate("MainWindow", "Nombre"))
        self.rbtn_sortCreationDate.setText(_translate("MainWindow", "Fecha de creación"))
        self.sort_includeSubfolder.setText(_translate("MainWindow", "Incluir subcarpetas"))
        self.btn_loadFolderFiles.setText(_translate("MainWindow", "Cargar archivos"))
        self.btn_ShowPicture.setText(_translate("MainWindow", "Mostrar Imagen"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.btn_sortTableRise.setText(_translate("MainWindow", "Subir"))
        self.btn_sortTableAddSeparator.setText(_translate("MainWindow", "Separador"))
        self.btn_sortTableDelete.setText(_translate("MainWindow", "Eliminar"))
        self.btn_sortTableDescend.setText(_translate("MainWindow", "Bajar"))
        item = self.table_filesList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
