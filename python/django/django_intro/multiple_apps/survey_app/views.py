# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    return HttpResponse("placeholder to display all the surveys created")


def new(request):
    return HttpResponse("placeholder for users to add a new survey")
