from django.shortcuts import render
from django.http import HttpResponse


# HOME PAGE
def home(request):
    return HttpResponse('Home Page')


# ABOUT PAGE
def about(request):
    return HttpResponse('About Page')