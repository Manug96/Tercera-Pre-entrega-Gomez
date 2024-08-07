from appcoder.forms import ProductoFormulario, SearchForm
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
            nombre=request.POST['productos'], comision=request.POST['comision'], email=request.POST['email'])
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


def buscar_productos(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Productos.objects.filter(nombre__icontains=query)
            return render(request, "appcoder/resultado_busqueda.html", {"form": form, "resultados": resultados, "query": query, "busqueda_realizada": True})
    else:
        form = SearchForm()
    return render(request, "appcoder/buscar_productos.html", {"form": form, "busqueda_realizada": False})
