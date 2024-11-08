from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request,'portfolio/contact.html')