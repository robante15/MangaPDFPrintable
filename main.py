from src.pdf_generation import makepdf
from src.img_splitter import IMGSplitter
from src.configuration_utils import ConfigUtils
from src.test_class import Alumno as alm

def main():
    #print('Hello World')
    #makepdf('output/GT-T01v2.pdf')
    #IMGSplitter.identify_split_folder('input')
    alumno = alm()
    alumno.nombre = 'Roberto'
    print(alumno.nombre)
    alumno.saludar()
    
if __name__ == '__main__':
    main()