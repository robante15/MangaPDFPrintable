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
WORKING_ARRAY: list = []


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # General
        self.statusbar.showMessage('Preparado')
        # Pestaña 1
        self.btn_openFolder.clicked.connect(self.OpenInputFolder)
        self.btn_selectSeparator.clicked.connect(self.OpenSeparatorFile)
        self.btn_loadFolderFiles.clicked.connect(self.LoadFolderFiles)
        self.table_filesList.itemClicked.connect(self.TablePreviewClickEvent)
        self.btn_sortTableRise.clicked.connect(self.moveUp_filesList)
        self.btn_sortTableDescend.clicked.connect(self.moveDown_filesList)
        self.btn_sortTableDelete.clicked.connect(
            self.deleteCurrentRow_filesList)
        self.btn_sortTableAddSeparator.clicked.connect(self.addSeparator)
        self.btn_sortMainList.clicked.connect(self.sort_filesList)
        self.btn_fileListOK.clicked.connect(self.fileListOk)

        # Pestaña 2
        self.btn_loadHorizontal.clicked.connect(self.loadHorizontalFiles)
        self.btn_splitFiles.clicked.connect(self.splitFilesAction)
        self.table_horizontalList.itemClicked.connect(
            self.TableHorizontalClickEvent)
        self.table_splitedFiles.itemClicked.connect(
            self.TableSplitedFilesClickEvent)

        self.table_SortedSplitedFiles.itemClicked.connect(
            self.TableSplitedSortedClickEvent)

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

    def addSeparator(self):
        separator = os.path.split(self.txt_separatorPath.text())
        filesOk = TH.filesOnTableArray(self.table_filesList)
        row = self.table_filesList.currentRow() + 1
        filesOk.insert(row, [separator[1], separator[0]])
        TH.cleanTable(self.table_filesList)
        TH.fillTable(filesOk, self.table_filesList)

    def fileListOk(self):
        global INPUT_DIRECTORY
        global WORKING_DIRECTORY
        global WORKING_ARRAY

        if self.table_filesList.rowCount() != 0:
            WORKING_ARRAY = TH.filesOnTableArray(self.table_filesList)
            FileUtils.copyFilesToFolder(WORKING_ARRAY, WORKING_DIRECTORY)
            WORKING_ARRAY = FileUtils.changeDirectoryFileList(
                WORKING_ARRAY, WORKING_DIRECTORY)
            TH.cleanTable(self.table_filesList)
            TH.fillTable(WORKING_ARRAY, self.table_filesList)
        else:
            self.statusbar.showMessage(
                'Error: Debes de seleccionar archivos primero')

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

    def OpenSeparatorFile(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Seleccionar separador', INPUT_DIRECTORY, "Image files (*.jpg *.gif *.png *.jpeg)")
        self.txt_separatorPath.setText(fname[0])

    def OpenWokingFolder(self):
        """Abre el directorio desde el cual se van a almacenar los archivos de imagen utilizados
        """
        folder = str(QFileDialog.getExistingDirectory(
            self, "Selecciona un directorio"))
        global WORKING_DIRECTORY
        WORKING_DIRECTORY = folder
        self.txt_workingDirectory.setText(WORKING_DIRECTORY)
        self.statusbar.showMessage('Directorio: ' + INPUT_DIRECTORY)

    def LoadFolderFiles(self):
        """Lee los archivos del directorio dado y popula la tabla con sus nombres
        """
        global WORKING_ARRAY
        if self.txt_inputFolder.text() != '':
            WORKING_ARRAY = FileUtils.readFolderFiles(
                self.txt_inputFolder.text())
            TH.cleanTable(self.table_filesList)
            TH.fillTable(WORKING_ARRAY, self.table_filesList)
        else:
            self.statusbar.showMessage(
                'Error: Primero debes de seleccionar un directorio')

    def TablePreviewClickEvent(self):
        row = self.table_filesList.currentRow()
        image_path = self.table_filesList.item(row, 0).text()
        image_directory = self.table_filesList.item(row, 2).text()
        GFXHelper.loadPreview(image_directory+'/' +
                              image_path, self.gfx_Preview)

    def TableHorizontalClickEvent(self):
        row = self.table_horizontalList.currentRow()
        image_path = self.table_horizontalList.item(row, 0).text()
        image_directory = self.table_horizontalList.item(row, 2).text()
        GFXHelper.loadPreview(image_directory+'/' +
                              image_path, self.gfx_splitPreview)

    def TableSplitedFilesClickEvent(self):
        row = self.table_splitedFiles.currentRow()
        image_path = self.table_splitedFiles.item(row, 0).text()
        image_directory = self.table_splitedFiles.item(row, 2).text()
        GFXHelper.loadPreview(image_directory+'/' +
                              image_path, self.gfx_splitPreview)

    def TableSplitedSortedClickEvent(self):
        row = self.table_SortedSplitedFiles.currentRow()
        image_path = self.table_SortedSplitedFiles.item(row, 0).text()
        image_directory = self.table_SortedSplitedFiles.item(row, 1).text()
        GFXHelper.loadPreview(image_directory+'/' +
                              image_path, self.gfx_splitPreview)

    def loadHorizontalFiles(self):
        global WORKING_ARRAY
        HorizontalFiles = []
        indice = 0
        for file in WORKING_ARRAY:
            orientation = IMGSplitter.check_orientation(
                file[1] + '/' + file[0])
            if orientation == 'H':
                file_plus_directory = [file[0], file[1], indice]
                HorizontalFiles.append(file_plus_directory)
            indice += 1
        TH.fillTable(HorizontalFiles, self.table_horizontalList, True)

    def splitFilesAction(self):
        horizontalFiles: list = TH.filesOnTableArray(
            self.table_horizontalList, True)
        global WORKING_DIRECTORY
        global WORKING_ARRAY

        splitedFilesArray:list = []
        auxiliarDupplaArray:list = []
        backupFolder = WORKING_DIRECTORY + '/' + 'originalH'

        for file in horizontalFiles:
            absFile = file[1] + '/' + file[0]
            fileIndex = int(file[2])-1
            imB, imA = IMGSplitter.splitImage(
                absFile, fileIndex, True, WORKING_DIRECTORY, backupFolder)
            auxiliarDupla = [imA, imB]
            auxiliarDupplaArray.append(auxiliarDupla)
            splitedFilesArray.append(imA)
            splitedFilesArray.append(imB)

        FileUtils.changeDirectoryFileList(horizontalFiles, backupFolder)
        TH.cleanTable(self.table_horizontalList)
        TH.fillTable(horizontalFiles, self.table_horizontalList, True)

        TH.fillTable(splitedFilesArray, self.table_splitedFiles, True)

        WORKING_ARRAY = FileUtils.addSplitedToArray(WORKING_ARRAY, auxiliarDupplaArray)
        TH.fillTable(WORKING_ARRAY, self.table_SortedSplitedFiles, directoryCol=1)


# ----------------------- Pestaña 3 / Generación del PDF ----------------------- #


    def generatePDFAction(self):
        global WORKING_DIRECTORY
        global WORKING_ARRAY
        '''MakePDFArray = FileUtils.readFolderFiles(WORKING_DIRECTORY)
        MakePDFArray.sort()
        indice = 0
        for file in MakePDFArray:
            MakePDFArray[indice] = WORKING_DIRECTORY + '/' + file
            indice += 1'''
        PDFName = self.txt_pdfName.text() + '.pdf'
        PDFGeneration.makepdf(WORKING_ARRAY, PDFName)
