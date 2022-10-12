from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1>Welcome to the website!</h1>")
