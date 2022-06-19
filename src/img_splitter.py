# Importing Image class from PIL module
from PIL import Image
from src.file_utils import FileUtils
import os
import shutil

class IMGSplitter():
    def check_orientation(image_file: str):
        '''
        Comprueba la orientación de un archivo de imágen. 
        Si es Horizontal retorna "H", si es Vertical retorna "V"
        '''
        temp_img = Image.open(image_file)
        width, height = temp_img.size
        proportion = width / height
        if proportion > 1:
            return 'H'
        if proportion <= 1:
            return 'V'


    def splitImage(image_file: str, split_and_replace: bool = True, output_folder: str = '.temp'):
        '''
        Corta una imagen a la mitad generando dos archivos, la parte A (Der) y la parte B (Izq)
        '''
        dirname, filename = os.path.split(os.path.abspath(image_file))
        im_name, im_ext = os.path.splitext(filename)
        # Abre una imagen en modo RGB
        im = Image.open(image_file)

        # Tamaño de la imagen en píxeles (tamaño de la imagen original)
        width, height = im.size

        # Configuración de los puntos para la imagen recortada
        first_half = 0, 0, width/2, height

        # Configuración de los puntos para la imagen recortada
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
        im1.save(output_folder+'/'+im1_name)
        im2.save(output_folder+'/'+im2_name)

        if split_and_replace == True:
            os.remove(image_file)
            shutil.move(output_folder+'/'+im1_name, dirname+'/'+im1_name)
            shutil.move(output_folder+'/'+im2_name, dirname+'/'+im2_name)


    def identify_split_folder(folder: str, split_and_replace: bool = True, output_folder: str = '.temp'):
        '''
        Dado un directorio dado identifica las imagenes horizontales y las corta por mitad
        '''
        directory_files = []
        progress = 0

        for path in os.listdir(folder):
            # check if current path is a file
            if os.path.isfile(os.path.join(folder, path)):
                # directory_files.append(path)
                directory_files.append(os.path.join(folder, path))

        step = 1 / len(directory_files)
        for file in directory_files:
            if(FileUtils.check_orientation(file) == 'H'):
                FileUtils.splitImage(file, split_and_replace, output_folder)
            progress += step
            print('Avance: '+"{0:.1%}".format(progress))

        if split_and_replace == True:
            try:
                os.rmdir(output_folder)
            except:
                print("No hay directorio")


#identify_split_folder('split')
# check_folder_exisist('.temp')
