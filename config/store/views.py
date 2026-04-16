from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'id':1,
    }
    return HttpResponse(context)
