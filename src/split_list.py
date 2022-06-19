import os

class SplitList():
    # Separa el listado en chunks de un numero dado de elementos
    def chunk_list(list, chunk_size):
        chunked_list = []
        for i in range(0, len(list), chunk_size):
            chunked_list.append(list[i:i+chunk_size])
        return chunked_list

    # Rellena el listado con los elementos faltantes
    def fill_chunked_list(chunked_list, filler=4, fillment='blank.jpg'):
        list_index = 0

        for chunk in chunked_list:
            #print(chunk, list_index)
            if len(chunk) < 4:
                lack = filler - len(chunk)
                # print(lack)
                for x in range(lack):
                    chunked_list[list_index].append('resources/blank.png')
            list_index += 1

    # Ordena las sublistas con el patrón 1-4-3-2
    def sort_pattern(filled_list):
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

    def order_folder(directory, chunk_size = 4):
        directory_files = []
        for path in os.listdir(directory):
            # check if current path is a file
            if os.path.isfile(os.path.join(directory, path)):
                #directory_files.append(path)
                directory_files.append(os.path.join(directory, path))

        chuncked_list = SplitList.chunk_list(directory_files, chunk_size)
        SplitList.fill_chunked_list(chuncked_list)
        SplitList.sort_pattern(chuncked_list)
        return chuncked_list

#listado_ordenado = order_folder('DS62')
#print(listado_ordenado)