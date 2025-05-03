from django import forms
from .models import DetalleGasto, Evento, Proveedor

class DetalleGastoForm(forms.ModelForm):
    class Meta:
        model = DetalleGasto
        fields = ['importe', 'concepto', 'tipo_gasto', 'proveedor', 'comentarios']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 600px;'}),
            #'descripcion': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 600px;'}),
            # Repite para los campos que quieras ajustar
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto']

