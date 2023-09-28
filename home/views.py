from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def css_assignment(request):
    return render(request, 'css_assignment.html')