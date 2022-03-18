from urllib import request
from django.shortcuts import render

# Create your views here.

def HomePage(request, **kwargs):
    return render(request, 'pages/home_page.html')
