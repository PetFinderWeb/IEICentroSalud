import os
from Euskadi.settings import MEDIA_ROOT
import json
from django.http import JsonResponse


def cargar_json(request):
    # abrir con encoding utf8 para las tildes
    with open(os.path.join(MEDIA_ROOT, 'bibliotecas.json'), 'r', encoding='utf-8') as file:
        return JsonResponse(json.load(file), safe=False)
