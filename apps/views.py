from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def BASE(request):
    return render(request, 'base/base.html')

# def index(request):
#     return render(request,'base/index2.html')