from django.urls import path

from appcoder.views import inicio, productos, historia, redes, ProductosFormulario, form_con_api, buscar_productos


urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos', productos, name="productos"),
    path('historia', historia, name="historia"),
    path('redes', redes, name="redes"),
    path('ProductosFormulario', ProductosFormulario, name="ProductosFormulario"),
    path('form-con-api/', form_con_api, name="formconapi"),

    path('buscar/', buscar_productos, name='buscar_productos'),



]
