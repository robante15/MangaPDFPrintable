from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


from gui.mainWindow import Ui_MainWindow
from gui.table_helpers import TableHelpers as TH
from gui.gfx_preview_helper import GFXHelper
from src.img_splitter import IMGSplitter
from src.file_utils import FileUtils

WORKING_DIRECTORY: str = ''


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # General
        self.statusbar.showMessage('Preparado')
        #Pestaña 1
        self.btn_openFolder.clicked.connect(self.OpenFolder)
        self.btn_loadFolderFiles.clicked.connect(self.ScanFolderFiles)
        self.table_filesList.itemClicked.connect(self.TablePreviewClickEvent)
        self.table_horizontalList.itemClicked.connect(
            self.TableHorizontalClickEvent)
        self.btn_sortTableRise.clicked.connect(self.moveUp_filesList)
        self.btn_sortTableDescend.clicked.connect(self.moveDown_filesList)
        self.btn_sortTableDelete.clicked.connect(
            self.deleteCurrentRow_filesList)
        self.btn_loadHorizontal.clicked.connect(self.loadHorizontalFiles)
        self.btn_sortMainList.clicked.connect(self.sort_filesList)

        #Pestaña 2
        self.btn_splitFiles.clicked.connect(self.splitFilesAction)

    def deleteCurrentRow_filesList(self):
        TH.deleteCurrentRow(self.table_filesList)

    def moveUp_filesList(self):
        TH.moveUpCurrentRow(self.table_filesList)

    def moveDown_filesList(self):
        TH.moveDownCurrentRow(self.table_filesList)

    def sort_filesList(self):
        TH.sortFilesOnTable(self.table_filesList)

    def OpenFolder(self):
        """Abre el directorio desde el cual se van a leer los archivos del manga
        """
        folder = str(QFileDialog.getExistingDirectory(
            self, "Selecciona un directorio"))
        self.txt_inputFolder.setText(folder)
        global WORKING_DIRECTORY
        WORKING_DIRECTORY = folder
        self.statusbar.showMessage('Directorio: ' + WORKING_DIRECTORY)

    def ScanFolderFiles(self):
        """Lee los archivos del directorio dado y popula la tabla con sus nombres
        """
        if self.txt_inputFolder.text() != '':
            fUtils = FileUtils()
            files_array = fUtils.readFolderFiles(self.txt_inputFolder.text())
            TH.cleanTable(self.table_filesList)
            TH.fillTable(files_array, self.table_filesList)
        else:
            self.statusbar.showMessage(
                'Error: Primero debes de seleccionar un directorio')

    def TablePreviewClickEvent(self):
        row = self.table_filesList.currentRow()
        image_path = self.table_filesList.item(row, 0).text()
        global WORKING_DIRECTORY
        GFXHelper.loadPreview(WORKING_DIRECTORY+'/' +
                              image_path, self.gfx_Preview)

    def TableHorizontalClickEvent(self):
        row = self.table_horizontalList.currentRow()
        image_path = self.table_horizontalList.item(row, 0).text()
        global WORKING_DIRECTORY
        GFXHelper.loadPreview(WORKING_DIRECTORY+'/' +
                              image_path, self.gfx_splitPreview)

    

    def loadHorizontalFiles(self):
        selectedFiles = TH.filesOnTableArray(self.table_filesList)
        HorizontalFiles = []
        global WORKING_DIRECTORY
        for file in selectedFiles:
            orientation = IMGSplitter.check_orientation(
                WORKING_DIRECTORY + '/' + file)
            if orientation == 'H':
                HorizontalFiles.append(file)
        TH.fillTable(HorizontalFiles, self.table_horizontalList)

    def splitFilesAction(self):
        horizontalFiles: list = TH.filesOnTableArray(self.table_horizontalList)
        print(horizontalFiles)
