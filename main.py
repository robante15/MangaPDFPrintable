from src.pdf_generation import makepdf
from src.img_splitter import IMGSplitter
from src.configuration_utils import ConfigUtils


def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def main():
    '''Paso 1: Identificar las páginas dobles, y seccionarlas
    Paso 2: Eliminar páginas extras, agregar/quitar separadores, ver formato (Manual)
    Paso 3: Generar archivo PDF'''

    #cfgUtils = ConfigUtils()
    # cfgUtils.save_configs(cfgUtils.PDFMakingDefault,cfgUtils.OutputPDFDefault)
    # cfgUtils.read_actual_config()
    # print(cfgUtils.OutputPDFRunning['name'])

    salir = False
    opcion = 0

    while not salir:

        print("1. Cortar páginas dobles")
        print("2. Generar archivo PDF")
        print("3. Salir")

        print("Elige una opcion")

        opcion = pedirNumeroEntero()

        if opcion == 1:
            directorio = str(input("Ingresa el directorio: ") or 'input')
            IMGSplitter.identify_split_folder(directorio)
        elif opcion == 2:
            archivo = str(input("Nombre del PDF: ") or 'default.pdf')
            makepdf(archivo)
        elif opcion == 3:
            salir = True
        else:
            print("Introduce un numero entre 1 y 3")

    print("Fin")


if __name__ == '__main__':
    main()
