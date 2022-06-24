import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.mainWindow import Ui_MainWindow
from src.file_utils import FileUtils

working_directory: str = ''


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.statusbar.showMessage('Preparado')
        self.btn_openFolder.clicked.connect(self.OpenFolder)
        self.btn_loadFolderFiles.clicked.connect(self.ScanFolderFiles)
        self.table_filesList.itemClicked.connect(self.TableClickEvent)
        self.btn_sortTableRise.clicked.connect(self.moveUp)
        self.btn_sortTableDescend.clicked.connect(self.moveDown)
        self.btn_sortTableDelete.clicked.connect(self.deleteRow)
        self.btn_loadHorizontal.clicked.connect(self.selectedFilesArray)

    def OpenFolder(self):
        folder = str(QFileDialog.getExistingDirectory(
            self, "Selecciona un directorio"))
        self.txt_inputFolder.setText(folder)
        global working_directory
        working_directory = folder

    def ScanFolderFiles(self):
        if self.txt_inputFolder.text() != '':
            fUtils = FileUtils()
            files_array = fUtils.readFolderFiles(self.txt_inputFolder.text())
            self.cleanTable()
            for file in files_array:
                row = self.table_filesList.rowCount()
                self.table_filesList.setRowCount(row+1)
                cell = QTableWidgetItem(str(file))
                self.table_filesList.setItem(row, 0, cell)
        else:
            self.statusbar.showMessage(
                'Error: Primero debes de seleccionar un directorio')

    def TableClickEvent(self):
        row = self.table_filesList.currentRow()
        image_path = self.table_filesList.item(row, 0).text()
        global working_directory
        self.loadPreview(working_directory+'/'+image_path)

    def loadPreview(self, image_path: str):
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.gfx_Preview.setScene(scene)
            self.gfx_Preview.fitInView(
                scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def cleanTable(self):
        while (self.table_filesList.rowCount() > 0):
            self.table_filesList.removeRow(0)

    def moveDown(self):
        row = self.table_filesList.currentRow()
        column = self.table_filesList.currentColumn()
        if row < self.table_filesList.rowCount()-1:
            self.table_filesList.insertRow(row+2)
            for i in range(self.table_filesList.columnCount()):
                self.table_filesList.setItem(
                    row+2, i, self.table_filesList.takeItem(row, i))
                self.table_filesList.setCurrentCell(row+2, column)
            self.table_filesList.removeRow(row)

    def moveUp(self):
        row = self.table_filesList.currentRow()
        column = self.table_filesList.currentColumn()
        if row > 0:
            self.table_filesList.insertRow(row-1)
            for i in range(self.table_filesList.columnCount()):
                self.table_filesList.setItem(
                    row-1, i, self.table_filesList.takeItem(row+1, i))
                self.table_filesList.setCurrentCell(row-1, column)
            self.table_filesList.removeRow(row+1)

    def deleteRow(self):
        row = self.table_filesList.currentRow()
        self.table_filesList.removeRow(row)

    def addSeparator(self):
        row = self.table_filesList.currentRow()
        self.table_filesList.insertRow(row+1)

    def selectedFilesArray(self):
        selectedFiles = []
        for i in range(self.table_filesList.rowCount()):
            selectedFiles.append(self.table_filesList.item(i, 0).text())
        return selectedFiles
