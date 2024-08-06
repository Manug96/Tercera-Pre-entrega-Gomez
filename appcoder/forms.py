from django import forms


class ProductoFormulario(forms.Form):
    productos = forms.CharField()
    comision = forms.IntegerField()
    email = forms.EmailField()
