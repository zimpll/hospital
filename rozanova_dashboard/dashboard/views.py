from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'dashboard/index.html')
