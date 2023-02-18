import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from adverity.characters import Characters
from adverity.settings import BASE_DIR
from adverity.models import Collections

import os
import petl as etl
import datetime


def show_collections(request):
    collection_rows = Collections.objects.values_list()
    context = {
        'db_rows': collection_rows
    }
    return render(request, 'index.html', context)


def add_collection(request):
    characters = _extract_characters()
    csv_url = _save_characters_to_csv(characters)
    Collections(url=csv_url, created=datetime.datetime.now()).save()
    return JsonResponse({})


def _extract_characters():
    characters = Characters()
    characters.get_all()
    return characters.all_characters


def _save_characters_to_csv(characters):
    table = etl.fromdicts(characters.get('Characters'))
    csv_name = f"{str(uuid.uuid4())}.csv"
    path = os.path.join(BASE_DIR, "static", "adverity", "csvs", csv_name)
    _url = os.path.join("adverity", "csvs", csv_name)
    etl.tocsv(table, path)
    return _url
