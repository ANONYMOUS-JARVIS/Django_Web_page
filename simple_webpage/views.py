from django.shortcuts import render
from django.http import HttpResponse
from .models import knows


def home(request):
    know=knows()
    know.img='avatar-1.jpg'
    know.head='muthu'
    know.des='anonymous'

    return render(request,'home.html', {{konw}})

# Create your views here.
