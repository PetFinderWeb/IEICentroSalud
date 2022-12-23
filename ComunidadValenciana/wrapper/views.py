import csv
from django.http import JsonResponse
from django.shortcuts import render
import os
from ComunidadValenciana.settings import MEDIA_ROOT
from django.core import serializers


def cargar_csv(request):
    # abrir el fichero en modo lectura
    with open(os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv'), 'r') as file:
        res = []
        # parsear el fichero CSV como un diccionario
        datosDiccionario = csv.DictReader(file, delimiter=';')
        # recorrer el diccionario e insertarlo en una lista
        for row in datosDiccionario:
            res.append(row)
        # serializar la lista de los centros sanitarios
        return JsonResponse(res, safe=False)
