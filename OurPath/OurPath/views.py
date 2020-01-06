from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import os
import sys
import json
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