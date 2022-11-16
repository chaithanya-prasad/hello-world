from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HompageView(request):
    return HttpResponse("hello World!")