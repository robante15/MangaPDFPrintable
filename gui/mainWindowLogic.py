import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from gui.mainWindow import Ui_MainWindow
from gui.table_helpers import TableHelpers as TH
from gui.gfx_preview_helper import GFXHelper

from src.img_splitter import IMGSplitter
from src.file_utils import FileUtils
from src.pdf_generation import PDFGeneration

INPUT_DIRECTORY: str = ''
WORKING_DIRECTORY: str = ''


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # General
        self.statusbar.showMessage('Preparado')
        # Pestaña 1
        self.btn_openFolder.clicked.connect(self.OpenInputFolder)
        self.btn_loadFolderFiles.clicked.connect(self.ScanFolderFiles)
        self.table_filesList.itemClicked.connect(self.TablePreviewClickEvent)
        self.btn_sortTableRise.clicked.connect(self.moveUp_filesList)
        self.btn_sortTableDescend.clicked.connect(self.moveDown_filesList)
        self.btn_sortTableDelete.clicked.connect(self.deleteCurrentRow_filesList)
        self.btn_sortMainList.clicked.connect(self.sort_filesList)
        self.btn_fileListOK.clicked.connect(self.fileListOk)

        # Pestaña 2
        self.btn_splitFiles.clicked.connect(self.splitFilesAction)
        self.btn_loadHorizontal.clicked.connect(self.loadHorizontalFiles)
        self.table_horizontalList.itemClicked.connect(self.TableHorizontalClickEvent)
        self.table_splitedFiles.itemClicked.connect(self.TableSplitedFilesClickEvent)

        # Pestaña 3
        self.btn_generatePDF.clicked.connect(self.generatePDFAction)

    def deleteCurrentRow_filesList(self):
        TH.deleteCurrentRow(self.table_filesList)

    def moveUp_filesList(self):
        TH.moveUpCurrentRow(self.table_filesList)

    def moveDown_filesList(self):
        TH.moveDownCurrentRow(self.table_filesList)

    def sort_filesList(self):
        TH.sortFilesOnTable(self.table_filesList)

    def fileListOk(self):
        global INPUT_DIRECTORY
        global WORKING_DIRECTORY
        if self.table_filesList.rowCount() != 0:
            filesOk = TH.filesOnTableArray(self.table_filesList)
            FileUtils.copyFilesToFolder(filesOk, INPUT_DIRECTORY, WORKING_DIRECTORY)
        else:
            self.statusbar.showMessage('Error: Debes de seleccionar archivos primero')

    def OpenInputFolder(self):
        """Abre el directorio desde el cual se van a leer los archivos del manga
        """
        folder = str(QFileDialog.getExistingDirectory(
            self, "Selecciona un directorio"))
        self.txt_inputFolder.setText(folder)
        global INPUT_DIRECTORY
        INPUT_DIRECTORY = folder
        global WORKING_DIRECTORY
        WORKING_DIRECTORY = folder + '/temp'
        self.txt_pdfName.setText(os.path.basename(INPUT_DIRECTORY))
        self.txt_workingDirectory.setText(WORKING_DIRECTORY)
        self.txt_pdfInputDirectory.setText(WORKING_DIRECTORY)
        self.statusbar.showMessage('Directorio: ' + INPUT_DIRECTORY)

    def OpenWokingFolder(self):
        """Abre el directorio desde el cual se van a almacenar los archivos de imagen utilizados
        """
        folder = str(QFileDialog.getExistingDirectory(
            self, "Selecciona un directorio"))
        global WORKING_DIRECTORY
        WORKING_DIRECTORY = folder
        self.txt_workingDirectory.setText(WORKING_DIRECTORY)
        self.statusbar.showMessage('Directorio: ' + INPUT_DIRECTORY)

    def ScanFolderFiles(self):
        """Lee los archivos del directorio dado y popula la tabla con sus nombres
        """
        if self.txt_inputFolder.text() != '':
            files_array = FileUtils.readFolderFiles(self.txt_inputFolder.text())
            TH.cleanTable(self.table_filesList)
            TH.fillTable(files_array, self.table_filesList)
        else:
            self.statusbar.showMessage(
                'Error: Primero debes de seleccionar un directorio')

    def TablePreviewClickEvent(self):
        row = self.table_filesList.currentRow()
        image_path = self.table_filesList.item(row, 0).text()
        global INPUT_DIRECTORY
        GFXHelper.loadPreview(INPUT_DIRECTORY+'/' +
                              image_path, self.gfx_Preview)

    def TableHorizontalClickEvent(self):
        row = self.table_horizontalList.currentRow()
        image_path = self.table_horizontalList.item(row, 0).text()
        global WORKING_DIRECTORY
        GFXHelper.loadPreview(WORKING_DIRECTORY+'/' +
                              image_path, self.gfx_splitPreview)

    def TableSplitedFilesClickEvent(self):
        row = self.table_splitedFiles.currentRow()
        image_path = self.table_splitedFiles.item(row, 0).text()
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
        global WORKING_DIRECTORY
        splitedFilesPathArray = []
        splitedFilesArray = []
        
        for file in horizontalFiles:
            output = WORKING_DIRECTORY
            absFile = WORKING_DIRECTORY + '/' + file
            imB, imA = IMGSplitter.splitImage(absFile, True, output)
            splitedFilesPathArray.append(imA)
            splitedFilesPathArray.append(imB)
        
        for fileSplited in splitedFilesPathArray:
            splitedFilesArray.append(os.path.basename(fileSplited))
        TH.fillTable(splitedFilesArray, self.table_splitedFiles)     

# ----------------------- Pestaña 3 / Generación del PDF ----------------------- #
    def generatePDFAction(self):
        global WORKING_DIRECTORY
        MakePDFArray = FileUtils.readFolderFiles(WORKING_DIRECTORY)
        MakePDFArray.sort()
        indice = 0
        for file in MakePDFArray:
            MakePDFArray[indice] = WORKING_DIRECTORY + '/' + file
            indice+=1
        PDFName = self.txt_pdfName.text() + '.pdf'
        PDFGeneration.makepdf(MakePDFArray, PDFName)