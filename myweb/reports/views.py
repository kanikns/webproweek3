from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reportdoc(request):
    return HttpResponse('report doc')