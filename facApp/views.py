from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests


def home(request):
    # num = request.POST.get('num')
    # data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1} 
    # r = requests.get("http://127.0.0.1:8000/fact/", data)
    
    # json = r.json()
    # print(json)
    return render(request, "index.html")


# API
@api_view(["GET"])
def Factorial(number): # http://127.0.0.1:8000/fact/
    try:
        num = json.loads(number.body)
        sum = 1
        for x in range(1, num+1):
            sum *= x;
        
        return JsonResponse(str(sum), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_404_NOT_FOUND)