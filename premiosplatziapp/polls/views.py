from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

def index(request):             #Vinculamos nuestro view Index con el template index.html, para ver todas las preguntas
    """
    La estructura es de la siguiente manera, el render necesita 3 cosas: 
    (request, "ruta", "Dict con llave valor")
    En el diccionario va nuestra variable para mostrar todas las preguntas, ese es el Context.

    """

    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    context = {'question': question}
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta numero {question_id}")
