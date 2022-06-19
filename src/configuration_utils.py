import configparser
class ConfigUtils():
    configuracion = configparser.ConfigParser()

    def initial_config():
        ConfigUtils.configuracion['PDFMaking'] = {}
        PDFMaking = ConfigUtils.configuracion['PDFMaking']
        PDFMaking['landscape_mode'] = 'True'
        PDFMaking['paper_size'] = 'A4'
        PDFMaking['paper_width'] = '210'
        PDFMaking['paper_height'] = '178'
        PDFMaking['print_margin'] = '4.65'
        PDFMaking['middle_padding'] = '5'

        ConfigUtils.configuracion['OutputPDF'] = {}
        OutputPDF = ConfigUtils.configuracion['OutputPDF']
        OutputPDF['directory']='output'
        OutputPDF['name']='default.pdf'

        with open('config.cfg', 'w') as archivoconfig:
            ConfigUtils.configuracion.write(archivoconfig)

    def read_section(section:str):
        ConfigUtils.configuracion.read('config.cfg')
        return ConfigUtils.configuracion._sections[section]