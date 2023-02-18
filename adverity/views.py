import os
import uuid
import petl as etl
import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from adverity.characters import Characters
from adverity.table_formatter import TableFormatter
from adverity.settings import BASE_DIR
from adverity.models import Collections


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


def view_collection(request, _id, max_rows=10):
    if request.method == 'POST':
        headers = request.POST.getlist('headers')
        if not headers:
            return render(request, 'characters.html', _get_table_context(_id, max_rows))
        return render(request, 'duplicates.html', _get_table_duplicates_context(_id, headers))
    return render(request, 'characters.html', _get_table_context(_id, max_rows))


def _get_table_duplicates_context(csv_id, headers):
    etl_table = _get_table(csv_id)
    table = etl.cut(etl_table, headers)
    table = etl.transform.dedup.distinct(table, count='count')
    table_iterator = iter(table)
    headers = next(table_iterator)
    context = {
        'table_headers': headers,
        'table_rows': table_iterator,
        'table_id': csv_id
    }
    return context


def _get_table_context(csv_id, max_rows):
    etl_table = _get_table(csv_id)
    formatted_table = TableFormatter(etl_table, max_rows).format()
    table_iterator = iter(formatted_table)
    headers = next(table_iterator)
    context = {
        'table_headers': headers,
        'table_rows': table_iterator,
        'table_id': csv_id
    }
    return context


def _get_table(csv_id):
    collection = Collections.objects.get(id=csv_id)
    csv_path = os.path.join(BASE_DIR, "static", collection.url)
    return etl.fromcsv(csv_path)
