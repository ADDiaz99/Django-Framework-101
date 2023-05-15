from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there! Welcome to the polls area - WIP")

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta numero {question_id}")
