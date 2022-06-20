import configparser


class ConfigUtils:
    configuracion = configparser.ConfigParser()

    def __init__(self):
        self.PDFMakingRunning = {}
        self.OutputPDFRunning = {}
        self.ConfigurationSections = ['PDFMaking', 'OutputPDF']
        self.PDFMakingDefault = {'landscape_mode': 'True',
                                 'paper_size': 'A4', 'paper_width': '210',
                                 'paper_height': '178',
                                 'print_margin': '4.65',
                                 'middle_padding': '5'}

        self.OutputPDFDefault = {'directory': 'output',
                                 'name': 'default.pdf',
                                 'author': 'Lore Ipsum'}

    def save_configs(self, PDFMakingConfig, OutputPDFConfig):
        '''Guarda las configuraciones de PDFMaking, y OutputPDF'''
        ConfigUtils.configuracion['PDFMaking'] = {}
        PDFMaking = ConfigUtils.configuracion['PDFMaking']
        for clave in PDFMakingConfig:
            valor = PDFMakingConfig[clave]
            PDFMaking[clave] = valor

        ConfigUtils.configuracion['OutputPDF'] = {}
        OutputPDF = ConfigUtils.configuracion['OutputPDF']
        for clave in OutputPDFConfig:
            valor = OutputPDFConfig[clave]
            OutputPDF[clave] = valor

        with open('config.cfg', 'w') as archivoconfig:
            ConfigUtils.configuracion.write(archivoconfig)

    def read_section(self, section: str):
        ConfigUtils.configuracion.read('config.cfg')
        return ConfigUtils.configuracion._sections[section]

    def read_actual_config(self):
        self.OutputPDFRunning = self.read_section('OutputPDF')
        self.PDFMakingRunning = self.read_section('PDFMaking')
