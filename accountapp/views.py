from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 기존 장고 방식
def hello_world(request):
    return HttpResponse('hello_world!')

# 기존 장고 방식