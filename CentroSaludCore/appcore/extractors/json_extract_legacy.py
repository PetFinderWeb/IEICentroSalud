import json
import csv
from CentroSaludCore.settings import MEDIA_ROOT
from ..models import Establecimiento_Sanitario, Provincia, Localidad
from extractor import Extractor

class JSON_Extractor(Extractor):
    def handle_file(self):
        with open(MEDIA_ROOT + '/bibliotecas.json') as file:
            data = json.load(file)
            for raw_centro in data:
                provincia = self.get_save_provincia(raw_centro)
                localidad = self.get_save_localidad(raw_centro, provincia)
                centro = Establecimiento_Sanitario(
                    nombre = raw_centro.get('Nombre', ''),
                    tipo = raw_centro.get('Tipodecentro', ''),
                    direccion = raw_centro.get('Direccion', ''),
                    codigo_postal = raw_centro.get('Codigopostal', ''),
                    longitud = raw_centro.get('LONWGS84', 0.0),
                    latitud = raw_centro.get('LATWGS84', 0.0),
                    telefono = raw_centro.get('Telefono', ''),
                    descripcion = raw_centro.get('', ''),
                    en_localidad = localidad
                )
                provincia.save()
                localidad.save()
                centro.save()

    def get_save_localidad(self, raw_centro, provincia):
        codigos = self.getCodigosMunicipioProvincia()
        municipio = raw_centro.get('Municipio')
        try:
            localidad = Localidad.objects.get(
                        codigo__exact = codigos[municipio]['cod_muni']
                    )
        except Localidad.DoesNotExist:
            localidad = Localidad(
                        nombre = municipio,
                        codigo = codigos[municipio]['cod_muni'],
                        en_provincia = provincia
                    )
        return localidad

    def get_save_provincia(self, raw_centro):
        codigos = self.getCodigosMunicipioProvincia()
        municipio = raw_centro.get('Municipio')
        try:
            provincia = Provincia.objects.get(
                        codigo__exact = codigos[municipio]['cod_prov']
                    )
        except Provincia.DoesNotExist:    
            provincia = Provincia(
                        nombre = raw_centro.get('Provincia'),
                        codigo = codigos[municipio]['cod_prov']
                    )
        return provincia

    def add_mappings(self, codigos, mappings):
            for mapping in mappings:
                codigos[mapping[0]] = codigos[mapping[1]]

    def getCodigosMunicipioProvincia(self):
        with open(MEDIA_ROOT + '/tablaCodigosMunicipio.csv') as file_tablaCodigoMunicipio:
            reader = csv.reader(file_tablaCodigoMunicipio, delimiter=';')
            codigos = {line[2]: {'cod_muni' : str(line[1]), 'cod_prov': str(line[0])} for line in reader}
            self.add_mappings(codigos,[
                            ('Bidania-Goiatz','Bidegoian'),
                            ('Karrantza','Karrantza Harana/Valle de Carranza'),
                            ('Salvatierra','Salvatierra/Agurain'),
                            ('Arrasate','Arrasate/Mondragón'),
                            ('BARAKALDO','Barakaldo'),
                            ('Mimetiz','Zalla'),
                            ('Soraluze-Placencia de Las Armas','Soraluze/Placencia de las Armas'),
                            ('Arratzua-Ubarrundia','Arrazua-Ubarrundia'),
                            ('Valdegobía','Valdegovía/Gaubea'),
                            ('Moreda de Araba','Moreda de Álava'),
                            ('Iruña Oka / Iruña de Oca','Iruña Oka/Iruña de Oca'),
                            ('Peñacerrada - Urizaharra','Peñacerrada-Urizaharra'),
                            ('Ribera Alta / Erriberagoitia','Erriberagoitia/Ribera Alta'),
                            ('Ribera Baja / Erribera Beitia','Ribera Baja/Erribera Beitia'),
                            ('Ubidea','Ubide'),
                            ('Villanueva de Araba / Eskuernaga','Villanueva de Ávila'),
                            ('Valdegovía','Valdegovía/Gaubea'),
                            ('Ezkio-itsaso','Ezkio-Itsaso'),
                            ('Abanto-Zierbana','Abanto y Ciérvana-Abanto Zierbena'),
                            ('Abanto-Zierbena','Abanto y Ciérvana-Abanto Zierbena'),
                            ('Valle de Trápaga - Trapagaran','Valle de Trápaga-Trapagaran'),
                            ('Leaburu-Txarama','Leaburu'),
                            ('Mendata ','Mendata'),
                            ('Munitibar -Arbatzegi Gerrikaitz','Munitibar-Arbatzegi Gerrikaitz'),
                            ('Urduña-Orduña','Urduña/Orduña'),
                            ('Ayala / Aiara','Ayala/Aiara'),
                            ('ZERAIN','Zerain'),
            ])

        return codigos