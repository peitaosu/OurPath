from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import os
import sys
import json
import uuid
from . import map

def index(request):
    context = {}
    return render(request, 'index.html', context)

def map(request):
    context = {}
    latitude = request.GET["latitude"]
    longitude = request.GET["longitude"]
    zoom = request.GET["zoom"]
    map = get_map_from_coordinate(latitude, longitude, zoom)
    return render(request, 'map.html', context)

def upload(request):
    context = {}
    uploaded_list = []
    for file_upload in request.FILES.getlist('pictures'):
        fs = FileSystemStorage()
        name = str(uuid.uuid4())
        uploaded_list.append(name)
        file_name = fs.save(name, file_upload)
    return render(request, 'index.html', context)
