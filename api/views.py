from django.http.response import JsonResponse
from django.shortcuts import render

def apiOverview(request):
    return JsonResponse("Api Overview first response", safe=False)
