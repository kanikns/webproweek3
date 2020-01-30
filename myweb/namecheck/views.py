from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def check(request):
    return HttpResponse('all subject that prof have to teavh student.')

def index(request):
    return HttpResponse('This is index.')