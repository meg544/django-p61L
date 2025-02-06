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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto']

