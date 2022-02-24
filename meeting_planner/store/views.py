from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there, mini store for food comming soon!!")

def detail(request):
    return HttpResponse("Hello there, details for the store comming soon!!")

def electronics(request):
    return HttpResponse("Hello there, welcome to the electronics page!!")