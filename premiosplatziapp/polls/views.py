from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there! Welcome to the polls area - WIP")
# Create your views here.
