from django.shortcuts import render
from django.http.response import HttpResponse


def ebooks(request):
    return HttpResponse('this is ebooks page')