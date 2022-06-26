# Importing Image class from PIL module
from PIL import Image
from src.file_utils import FileUtils
import os
import shutil


class IMGSplitter():
    def check_orientation(image_file: str):
        """Comprueba la orientación de un archivo de imágen. 

        Args:
            image_file (str): Archivo de imágen a detectar la orientación

        Returns:
            chr: Si es Horizontal retorna "H", si es Vertical retorna "V"
        """
        temp_img = Image.open(image_file)
        width, height = temp_img.size
        proportion = width / height
        if proportion > 1:
            return 'H'
        if proportion <= 1:
            return 'V'

    def splitImage(image_file: str, split_and_replace: bool = True, output_folder: str = '.temp'):
        """Corta una imagen a la mitad generando dos archivos, la parte A (Der) y la parte B (Izq)

        Args:
            image_file (str): Archivo de imágen sobre el cual realizar el corte
            split_and_replace (bool, optional): Sobreescribe el archivo, o lo guarda aparte. Defaults to True.
            output_folder (str, optional): Directorio de salida del archivo recortado. Defaults to '.temp'.

        Returns:
            im1_path (str): Ruta de la mitad B
            im1_path (str): Ruta de la mitad A
        """
        dirname, filename = os.path.split(os.path.abspath(image_file))
        im_name, im_ext = os.path.splitext(filename)
        # Abre una imagen en modo RGB
        im = Image.open(image_file)

        # Tamaño de la imagen en píxeles (tamaño de la imagen original)
        width, height = im.size

        # Configuración de los puntos para la primera mitad
        first_half = 0, 0, width/2, height

        # Configuración de los puntos para la segunda mitad
        second_half = width/2, 0, width, height

        # Imagen recortada del tamaño anterior
        # (No cambiará la imagen original)
        im1 = im.crop(first_half)
        im2 = im.crop(second_half)

        # Asignación de nuevos nombres para las nuevas imágenes
        im1_name = im_name + '_B' + im_ext
        im2_name = im_name + '_A' + im_ext

        # Comprueba si el directorio de salida existe
        FileUtils.check_folder_exisist(output_folder)

        # Guardado de las imagenes
        im1_path = output_folder+'/'+im1_name
        im2_path = output_folder+'/'+im2_name
        im1.save(im1_path)
        im2.save(im2_path)

        if split_and_replace == True:
            # os.remove(image_file)
            FileUtils.check_folder_exisist(dirname + '/originalH')
            shutil.move(image_file, dirname + '/originalH')
            shutil.move(output_folder+'/'+im1_name, dirname+'/'+im1_name)
            shutil.move(output_folder+'/'+im2_name, dirname+'/'+im2_name)

        return(im1_path, im2_path)

    def identify_split_folder(folder: str, split_and_replace: bool = True, output_folder: str = '.temp'):
        """Dado un directorio dado identifica las imagenes horizontales y las corta por mitad

        Args:
            folder (str): Directorio de entrada para realizar el Split
            split_and_replace (bool, optional): Sobreescribe los archivos, o los guarda aparte. Defaults to True.
            output_folder (str, optional): Directorio de salida de los archivos recortados. Defaults to '.temp'.
        """
        directory_files = []  # Array que contiene los archivos
        progress = 0  # Contador de progreso

        # Recorre todo el directorio dado, y añade los path al array de archivos
        for path in os.listdir(folder):
            # Cerificar si la ruta actual es un archivo
            if os.path.isfile(os.path.join(folder, path)):
                directory_files.append(os.path.join(folder, path))

        # Calcula el step de cada pasada en el ciclo para añadir al contador
        step = 1 / len(directory_files)

        # Recorre los archivos almacenados en el array, comprueba su orientación
        for file in directory_files:
            if(IMGSplitter.check_orientation(file) == 'H'):
                IMGSplitter.splitImage(file, split_and_replace, output_folder)
            progress += step
            print('Avance: '+"{0:.1%}".format(progress))

        if split_and_replace == True:
            try:
                os.rmdir(output_folder)
            except:
                print("No hay directorio")
