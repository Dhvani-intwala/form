from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    View to return the index page.
    """
    return render(request, 'home.html')
