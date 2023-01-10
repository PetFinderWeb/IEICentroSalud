import csv
from django.http import JsonResponse
from django.shortcuts import render
import os
from ComunidadValenciana.settings import MEDIA_ROOT
from django.core import serializers


def cargar_csv(request):
    # Si a la petición GET se añade el parámetro 'all' a true se cargará el fichero con todos los registros
    if request.GET.get('all', False) == 'true':
        path = 'directorio-de-bibliotecas-valencianas_2020.csv'
    # Cargar únicamente los de la demo
    else:
        path = 'establecimientos-sanitarios-CV.csv'
    # abrir el fichero en modo lectura
    with open(os.path.join(MEDIA_ROOT, path), 'r') as file:
        res = []
        # parsear el fichero CSV como un diccionario
        datosDiccionario = csv.DictReader(file, delimiter=';')
        # recorrer el diccionario e insertarlo en una lista
        for row in datosDiccionario:
            res.append(row)
        # serializar la lista de los centros sanitarios a JSON
        return JsonResponse(res, safe=False)
