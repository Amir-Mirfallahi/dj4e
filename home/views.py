from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'index.html', {'questions': Question.objects.all()})


def css_assignment(request):
    return render(request, 'css_assignment.html')


def owner(request):
    return HttpResponse("Hello, world. 542fc94a is the polls index.")


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return HttpResponse(question)


def results(request, question_id):
    answer = Answer.objects.get(question_id=question_id)
    return HttpResponse(answer)


def vote(request, question_id):
    answer = Answer.objects.get(question_id=question_id)
    return HttpResponse(answer.votes)
