from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. 20bbf91c is the polls index.")
