from django.contrib import admin
from .models import Productos, Historia, Redes


class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")


admin.site.register(Productos, ProductosAdmin)
admin.site.register(Historia)
admin.site.register(Redes)
