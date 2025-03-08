from django.shortcuts import render
from django.http.response import HttpResponse


def podcasts(requeest):
    return HttpResponse('this is podcasts page')
