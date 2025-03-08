from django.shortcuts import render
from django.http.response import HttpResponse

def magazines(requests):
    return HttpResponse('this is magazines page')

