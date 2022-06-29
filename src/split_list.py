from calendar import c
import os


class SplitList():
    '''Clase encargada de manipular los chunks y el orden de los archivos para la generación del PDF'''

    def chunk_list(list: list, chunk_size: int):
        """Separa el listado completo, en chunks de tamaño X de elementos

        Args:
            list (list): Listado a ordenar
            chunk_size (int): Tamaño de los chunks en que se desea seccionar

        Returns:
            chunked_list (list): Listado ya seccionado en chunks
        """
        chunked_list = []
        for i in range(0, len(list), chunk_size):
            chunked_list.append(list[i:i+chunk_size])
        return chunked_list

    def fill_chunked_list(chunked_list: list, filler: int = 4, fillment: list = ['blank.png', 'resources']):
        """Rellena el listado con los elementos faltantes

        Args:
            chunked_list (list): Lista que contiene los chunks
            filler (int, optional): Cada cuantas posiciones se va a rellenar. Defaults to 4.
            fillment (str, optional): Con que elemento se va a rellenar. Defaults to 'resources/blank.png'.
        """
        list_index = 0
        # Recorre todos los chunks, si un chunk tiene una longitud menos a 4 lo rellena
        for chunk in chunked_list:
            if len(chunk) < filler:
                lack = filler - len(chunk)
                for x in range(lack):
                    chunked_list[list_index].append(fillment)
            list_index += 1

    def sort_pattern(filled_list: list):
        """Ordena las sublistas con el patrón 1-4-3-2

        Args:
            filled_list (list): Lista ya chunkeada, y posteriormente rellenada
        """
        index = 0
        for list in filled_list:
            # Ordenar lista
            auxiliary_list = [None]*4
            indice = 0
            for x in list:
                if indice == 0:
                    auxiliary_list[0] = x
                if indice == 1:
                    auxiliary_list[3] = x
                if indice == 2:
                    auxiliary_list[2] = x
                if indice == 3:
                    auxiliary_list[1] = x
                indice += 1
            filled_list[index] = auxiliary_list
            index += 1

    def order_folder(directory: str, chunk_size: int = 4):
        """Crea una lista con huecos rellenados, y aplicado el patrón 1-4-3-2

        Args:
            directory (str): Directorio desde donde se va a realizar el chunkeo
            chunk_size (int, optional): tamaño de los chunks. Defaults to 4.

        Returns:
            chuncked_list (list): Lista ya chunkeada
        """
        directory_files = []
        for path in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, path)):
                directory_files.append(os.path.join(directory, path))

        chuncked_list: list = SplitList.chunk_list(directory_files, chunk_size)
        SplitList.fill_chunked_list(chuncked_list)
        SplitList.sort_pattern(chuncked_list)
        return chuncked_list

    def order_list(source_list: list, chunk_size: int = 4):
        chuncked_list: list = SplitList.chunk_list(source_list, chunk_size)
        SplitList.fill_chunked_list(chuncked_list)
        SplitList.sort_pattern(chuncked_list)
        return chuncked_list
