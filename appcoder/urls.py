from django.urls import path

from appcoder.views import inicio, productos, historia, redes


urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos', productos, name="productos"),
    path('historia', historia, name="historia"),
    path('redes', redes, name="redes"),

]
