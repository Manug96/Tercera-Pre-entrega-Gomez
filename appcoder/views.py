from appcoder.forms import ProductoFormulario
from appcoder.models import Productos
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


def ProductosFormulario(request):

    if request.method == "POST":
        productos = Productos(
            nombre=request.POST['productos'], comision=request.POST['comision'])
        productos.save()

        return render(request, "appcoder/inicio.html")
    return render(request, "appcoder/ProductosFormulario.html")


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = ProductoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            productos = Productos(
                nombre=informacion["productos"], comision=informacion["comision"], email=informacion["email"])

            productos.save()

            return render(request, "appcoder/inicio.html")

    else:
        mi_formulario = ProductoFormulario()

    return render(request, "appcoder/form_con_api.html", {"mi_formulario": mi_formulario})


def busquedaproducto(request):
    if request.method == "POST":
        mi_formulario = busquedaproductoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            productos = Productos.objects.filter(
                nombre_icontains=informacion["productos"])

            return render(request, "appcoder/resultados_busquedaproducto.html", {"mi_formulario": mi_formulario})


def buscar(request):
    respuesta = f"Estoy en el Producto:{request.GET}['Producto']"

    return HttpResponse(respuesta)
