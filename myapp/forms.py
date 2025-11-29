from django import forms
from .models import DetalleGasto, Evento, Proveedor, Concepto, Categoria


class DetalleGastoForm(forms.ModelForm):
    class Meta:
        model = DetalleGasto
        fields = ['importe', 'concepto', 'tipo_gasto', 'concepto2', 'proveedor', 'comentarios']
        labels = {
            'concepto': 'Método de Pago',  # 👈 CAMBIO SOLO VISUAL
        }
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



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ConceptoForm(forms.ModelForm):
    class Meta:
        model = Concepto
        fields = ['concepto', 'estatus', 'categoria']

        widgets = {
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'estatus': forms.CheckboxInput(),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class DetalleGastoFormSinEvento(forms.ModelForm):
    class Meta:
        model = DetalleGasto
        fields = ['importe', 'concepto', 'tipo_gasto',
                  'concepto2', 'proveedor', 'comentarios']
        labels = {'concepto': 'Método de Pago',  # 👈 CAMBIO SOLO VISUAL
                 }