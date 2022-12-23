import os
from Euskadi.settings import MEDIA_ROOT
import json
from django.http import JsonResponse


def cargar_json(request):
    # Cargar todos los registros o únicamente los de la demo
    if request.GET.get('all', False) == 'true':
        path = 'bibliotecas.json'
    else:
        path = 'establecimientos-sanitarios-EUS.json'
    # abrir con encoding utf8 para las tildes
    with open(os.path.join(MEDIA_ROOT, path), 'r', encoding='utf-8') as file:
        return JsonResponse(json.load(file), safe=False)
