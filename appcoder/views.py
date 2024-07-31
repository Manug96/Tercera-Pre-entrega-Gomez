from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, "appcoder/inicio.html")


def productos(request):
    return render(request, "appcoder/productos.html")


def historia(request):
    return render(request, "appcoder/historia.html")


def redes(request):
    return render(request, "appcoder/redes.html")
