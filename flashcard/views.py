import csv, io
from django.shortcuts import render
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import KanjiN2
    

# upload file csv
@require_http_methods(["GET", "POST"])
@login_required(login_url="/admin/login/?next=/admin/")
def csv_upload(request, table):
    template = "csv_upload.html"
    model = table

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string) # skip the first line
    for column in csv.reader(io_string, delimiter =';', quotechar="|"):
        _, created = KanjiN2.objects.update_or_create(
            week = column[0],
            unit = column[1],
            main_word = column[2],
            meanning = column[3],
            defaults={'kotoba' : column[4]}
        )
        # print(column[4])
    context = {}
    return render(request, template, context)

@require_http_methods(["GET"])
def data_all(request, table):
    data = []
    model = None    
    if table == "kanjin2":
        model = KanjiN2

    data = model.objects.all().values()
    for item in data:
        item['kotoba'] = json.loads(item['kotoba'])
    return JsonResponse(list(data), safe=False)

@require_http_methods(["GET"])
def data_detail(request, table):
    url_params = request.GET
    data = []
    model = None
    filters = {}

    print(url_params)
    #get model for filter
    if table == "kanjin2":
        model = KanjiN2

    #get condition filter to look up in model
    if  'week' in url_params and url_params['week']:
        filters['week'] = url_params.get('week')
    if 'unit' in url_params and url_params['unit']:
        filters['unit'] = url_params.get('unit')
    if 'pk' in url_params and url_params['pk']:
        filters['pk'] = url_params.get('pk')

    data = model.objects.filter(**filters).values()
    for item in data:
        item['kotoba'] = json.loads(item['kotoba'] )
    return JsonResponse(list(data), safe=False)

