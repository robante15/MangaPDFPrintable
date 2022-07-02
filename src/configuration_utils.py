from configparser import ConfigParser
import json

PARSER = ConfigParser()
PARSER.read('config.cfg')


class ConfigUtils():
    #----------------------- MANGA CONFIGS -----------------------#
    def addManga(mangas_array: list, name: str, width: float, height: float):
        new_manga = {"nombre": name, "width": width, "height": height}
        mangas_array.append(new_manga)

    def saveManga(mangas_array: list):
        global PARSER
        PARSER['MANGA_SIZES']['sizes'] = json.dumps(mangas_array)
        with open('config.cfg', 'w') as configfile:
            PARSER.write(configfile)

    def readMangasSizesList():
        global PARSER
        return json.loads(PARSER['MANGA_SIZES']['sizes'])

    def getMangaSizeByName(mangas_array: list, manga_name: str):
        filtrado = list(
            filter(lambda manga: manga['nombre'] == manga_name, mangas_array))
        return(filtrado[0]['width'], filtrado[0]['height'])

    def getMangaSizeByIndex(mangas_array: list, manga_index: int):
        return(mangas_array[manga_index]['width'], mangas_array[manga_index]['height'])

    def getMangaByIndex(mangas_array: list, manga_index: int):
        return(mangas_array[manga_index]['nombre'], mangas_array[manga_index]['width'], mangas_array[manga_index]['height'])
