from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):             #Vinculamos nuestro view Index con el template index.html, para ver todas las preguntas
    """[polls/views/index]
    Args:
        request ([HTTP]): [Request]
    Returns:
        [Render]: [Request, Url, Dict(Question.objects.all())]
    """
    
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta numero {question_id}")
