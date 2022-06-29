from xmlrpc.client import Boolean
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap


class TableHelpers():
    def cleanTable(table: QTableWidget):
        """Elimina todos los registros de una table

        Args:
            table (QTableWidget): Tabla que se va a limpiar
        """
        while (table.rowCount() > 0):
            table.removeRow(0)

    def fillTable(filesArray: list, table: QTableWidget, splitTable = False, directoryCol:int = 2):
        """Rellena una tabla con un array unidimensional con el nombre del archivo de imágen

        Args:
            filesArray (list): Listado de archivos [archivo.ext, directorio]
            table (QTableWidget): Tabla que se va a popular
        """
        for file in filesArray:
            fila = table.rowCount()
            table.setRowCount(fila+1)
            
            celda = QTableWidgetItem(str(file[0]))
            table.setItem(fila, 0, celda)
            
            celda = QTableWidgetItem(str(file[1]))
            table.setItem(fila, directoryCol, celda)
            
            if splitTable:
                celda = QTableWidgetItem(str(int(file[2])+1))
                table.setItem(fila, 3, celda)
            '''label = QLabel()
            pixmap = QPixmap('resources/X_sep.png')
            label.setPixmap(pixmap)
            table.setItem(row, 1, label)'''

    def deleteCurrentRow(table: QTableWidget):
        """Elimina una fila de la tabla

        Args:
            table (QTableWidget): Tabla sobre la que se va a ejecutar la acción
        """
        row = table.currentRow()
        table.removeRow(row)

    def filesOnTableArray(table: QTableWidget, getIndex = False):
        """Retorna los nombres de los archivos en una table

        Args:
            table (QTableWidget): Tabla sobre la que se va a ejecutar la acción

        Returns:
            filesOnTable (list): Listado de archivos en la tabla [archivo.ext, directorio]
        """
        filesOnTable: list = []
        for i in range(table.rowCount()):
            if getIndex == False:
                files_plus_path = [table.item(i, 0).text(), table.item(i, 2).text()]
            else:
                files_plus_path = [table.item(i, 0).text(), table.item(i, 2).text(), table.item(i,3).text()]
            filesOnTable.append(files_plus_path)
        return filesOnTable

    def sortFilesOnTable(table: QTableWidget, rev: Boolean = False):
        """Ordena la tabla de manera ascendente o descendente

        Args:
            table (QTableWidget): Tabla sobre la que se va a ejecutar la acción
            rev (Boolean, optional): Sentido del ordenamiento True=Descendente, False=Ascendente. Defaults to False.
        """
        selectedFiles: list = TableHelpers.filesOnTableArray(table)
        selectedFiles.sort(reverse=rev)
        TableHelpers.cleanTable(table)
        TableHelpers.fillTable(selectedFiles, table)

    def moveDownCurrentRow(table: QTableWidget):
        """Mueve la fila seleccionada hacia arriba

        Args:
            table (QTableWidget): Tabla sobre la que se va a ejecutar la acción
        """
        row = table.currentRow()
        column = table.currentColumn()
        if row < table.rowCount()-1:
            table.insertRow(row+2)
            for i in range(table.columnCount()):
                table.setItem(
                    row+2, i, table.takeItem(row, i))
                table.setCurrentCell(row+2, column)
            table.removeRow(row)

    def moveUpCurrentRow(table: QTableWidget):
        """Mueve la fila seleccionada hacia abajo

        Args:
            table (QTableWidget): Tabla sobre la que se va a ejecutar la acción
        """
        row = table.currentRow()
        column = table.currentColumn()
        if row > 0:
            table.insertRow(row-1)
            for i in range(table.columnCount()):
                table.setItem(
                    row-1, i, table.takeItem(row+1, i))
                table.setCurrentCell(row-1, column)
            table.removeRow(row+1)

    '''def addSeparator():
        row = self.table_filesList.currentRow()
        self.table_filesList.insertRow(row+1)'''
