from django.shortcuts import render
from django.http.response import HttpResponse

def audiobooks(request):
    return HttpResponse('this is audiobooks page!!')
