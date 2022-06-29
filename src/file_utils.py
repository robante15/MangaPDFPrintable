import os
import shutil


class FileUtils():
    '''Funciones para manipulación de archivos o directorios'''
    # Comprueba si el directorio existe, si no existe lo crea
    def check_folder_exisist(folder_path: str):
        """Comprueba si el directorio existe. En caso contrario lo crea

        Args:
            folder_path (str): Directorio que se quiere comprobar si existe
        """
        isExist = os.path.exists(folder_path)
        if not isExist:
            os.makedirs(folder_path)

    def getFileNameExt(file_path: str):
        """Retorna el nombre y la extención del archivo dado

        Args:
            file_path (str): Dirección del archivo a evaluar
        """
        file_name = os.path.basename(file_path)
        return(os.path.splitext(file_name))

    def readFolderFiles(folder_path: str):
        """Lee los archivos dentro de un directorio y retorna un array con ellos

        Args:
            folder_path (str): Directorio de analisis

        Returns:
            files_array (list): Array que contiene un listado de archivos dentro del directorio [nombre.ext, directorio]
        """
        # Listado de archivos
        files_array: list = []

        # Iterate directory
        for path in os.listdir(folder_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(folder_path, path)):
                file_plus_path = [path, folder_path]
                files_array.append(file_plus_path)
        return files_array

    def changeDirectoryFileList(filesArray: list, newLocation: str):
        filesArrayTemp = filesArray
        for file in filesArrayTemp:
            file[1] = newLocation
        return filesArrayTemp

    def copyFilesToFolder(files_list: list, output: str):
        """Copia un listado de archivos desde un directorio de origen, a uno de destino

        Args:
            files_list (list): Listado de archivos a copiar [archivo.ext, directorio]
            output (str): Directorio de destino de los archivos
        """
        FileUtils.check_folder_exisist(output)
        for file in files_list:
            shutil.copy(file[1] + '/' + file[0], output)

    def moveFilesToFolder(files_list: list, files_directory: str, output: str):
        """Mueve un listado de archivos desde un directorio de origen, a uno de destino

        Args:
            files_list (list): Listado de archivos a mover
            files_directory (str): Directorio de origen de los archivos
            output (str): Directorio de destino de los archivos
        """
        FileUtils.check_folder_exisist(output)
        for file in files_list:
            shutil.move(files_directory + '/' + file, output)
    
    def addSplitedToArray(originalArray:list, duplaSplitedFilesArray:list):
        iterador = 0
        for duplaFiles in duplaSplitedFilesArray:
            originalArray.pop(duplaFiles[0][2] + iterador)
            originalArray.insert(duplaFiles[1][2] + iterador, duplaFiles[1])
            originalArray.insert(duplaFiles[0][2] + iterador, duplaFiles[0])
            iterador+=1
        return originalArray