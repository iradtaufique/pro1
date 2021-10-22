from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>Hello Word!</h1>')

def funct_abc(request):
    return HttpResponse('<h1>Hello ABC Page</h1>')


