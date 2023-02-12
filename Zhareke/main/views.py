from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Index Page</h1>")
def not_found(request,exception):
    return HttpResponse("Page tabylmady")