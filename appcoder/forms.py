from django import forms


class ProductoFormulario(forms.Form):
    productos = forms.CharField()
    comision = forms.IntegerField()
    email = forms.EmailField()


class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar Productos', max_length=100)
