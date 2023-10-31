from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response


# Create your views here.


# 기존 장고 방식
def hello_world(request):
    return HttpResponse('hello_world!')

# DRF 방식으로
def hello_world_drf(request):
    return Response({"message" : "hello_world!"})



