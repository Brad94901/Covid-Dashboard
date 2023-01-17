from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from pymongo import MongoClient
from utils import get_db_handle

def index( request ):
    # return HttpResponse("Hello, world. You're at the covid index.")
    return render( request, 'covid/index.html', {})
    
def technology( request ):
    return render(request, 'covid/technology.html', {})

def about( request ):
    return render(request, 'covid/about.html', {})