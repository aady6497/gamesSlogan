from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Welcome to the Games Site:{}".format(datetime.now()))