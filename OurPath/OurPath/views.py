from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import os
import sys
import json

def index(request):
    context = {}
    return render(request, 'index.html', context)
