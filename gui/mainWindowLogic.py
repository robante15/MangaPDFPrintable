import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.mainWindow import Ui_MainWindow
from src.img_splitter import IMGSplitter
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
        self.table_filesList.itemClicked.connect(self.TablePreviewClickEvent)
        self.table_horizontalList.itemClicked.connect(self.TableHorizontalClickEvent)
        self.btn_sortTableRise.clicked.connect(self.moveUp)
        self.btn_sortTableDescend.clicked.connect(self.moveDown)
        self.btn_sortTableDelete.clicked.connect(self.deleteRow)
        self.btn_loadHorizontal.clicked.connect(self.loadHorizontalFiles)

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
            self.cleanTable(self.table_filesList)
            self.fillTable(files_array, self.table_filesList)
        else:
            self.statusbar.showMessage(
                'Error: Primero debes de seleccionar un directorio')

    def TablePreviewClickEvent(self):
        row = self.table_filesList.currentRow()
        image_path = self.table_filesList.item(row, 0).text()
        global working_directory
        self.loadPreview(working_directory+'/'+image_path, self.gfx_Preview)

    def TableHorizontalClickEvent(self):
        row = self.table_horizontalList.currentRow()
        image_path = self.table_horizontalList.item(row, 0).text()
        global working_directory
        self.loadPreview(working_directory+'/'+image_path, self.gfx_splitPreview)

    def loadPreview(self, image_path: str, gfx_viewer: QGraphicsView):
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            gfx_viewer.setScene(scene)
            gfx_viewer.fitInView(
                scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def cleanTable(self, table: QTableWidget):
        while (table.rowCount() > 0):
            table.removeRow(0)

    def fillTable(self, filesArray: list, table: QTableWidget):
        for file in filesArray:
            row = table.rowCount()
            table.setRowCount(row+1)
            cell = QTableWidgetItem(str(file))
            table.setItem(row, 0, cell)

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

    def loadHorizontalFiles(self):
        selectedFiles = self.selectedFilesArray()
        HorizontalFiles = []
        global working_directory
        for file in selectedFiles:
            orientation = IMGSplitter.check_orientation(
                working_directory + '/' + file)
            if orientation == 'H':
                HorizontalFiles.append(file)
        self.fillTable(HorizontalFiles, self.table_horizontalList)

    def splitFilesAction(self):
        horizontalFiles = []
        for i in range(self.table_filesList.rowCount()):
            horizontalFiles.append(self.table_filesList.item(i, 0).text())
        return horizontalFiles