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

class ReportePagosForm(forms.Form):
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        label="Proveedor",
        required=True
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Desde",
        required=True
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Hasta",
        required=True
    )