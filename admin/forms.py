from django import forms
from Productos.models import Producto

class FormProducto(forms.ModelForm):
  class Meta:
    model = Producto
    fields = '__all__'