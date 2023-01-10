import os
from Euskadi.settings import MEDIA_ROOT
import json
from django.http import JsonResponse


def cargar_json(request):
    # Si a la petición GET se añade el parámetro 'all' a true se cargará el fichero con todos los registros
    if request.GET.get('all', False) == 'true':
        path = 'bibliotecas.json'
    # Cargar únicamente únicamente los de la demo
    else:
        path = 'establecimientos-sanitarios-EUS.json'
    # abrir con encoding utf8 para las tildes
    with open(os.path.join(MEDIA_ROOT, path), 'r', encoding='utf-8') as file:
        # Devolver los registros en JSON
        return JsonResponse(json.load(file), safe=False)
