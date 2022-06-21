import os


class FileUtils():
    '''Funciones para manipulación de archivos o directorios'''
    # Comprueba si el directorio existe, si no existe lo crea
    def check_folder_exisist(folder_path: str):
        '''
        Comprueba si el directorio existe.
        En caso contrario lo crea
        '''
        isExist = os.path.exists(folder_path)
        if not isExist:
            os.makedirs(folder_path)

    def getFileNameExt(file_location: str):
        '''
        Retorna el nombre y la extención del archivo dado
        '''
        file_name = os.path.basename(file_location)
        return(os.path.splitext(file_name))

    def readFolderFiles(self, folder_path:str):
        # list to store files
        files_array = []

        # Iterate directory
        for path in os.listdir(folder_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(folder_path, path)):
                files_array.append(path)
        return files_array