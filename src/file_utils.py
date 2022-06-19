import os


class FileUtils():
    # Comprueba si el directorio existe, si no existe lo crea
    def check_folder_exisist(folder_path: str):
        '''
        Comprueba si el directorio existe
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
