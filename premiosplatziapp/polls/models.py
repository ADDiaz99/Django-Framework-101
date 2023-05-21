import datetime

from django.db import models
from django.utils import timezone

#Creamos los modelos question y choice, recordemos que el ID viene por default gracias a Django

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):                      #Hacemos un metodo para que nos retorne la pregunta en Shell
        return self.question_text
    
    def was_published_recently(self):       #Hacemos otro metodo para checar si la pregunta ha sido publicada hace menos de un dia
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) #le restamos al tiempo actual 1 dia y lo verificamos si es mayor al pubdate

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #El on_delete nos permite borrar todas las respuestas si se borra la pregunta
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
