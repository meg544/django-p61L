from django import forms
from .models import DetalleGasto, Evento, Proveedor, Concepto, Categoria, Graduado


class DetalleGastoForm(forms.ModelForm):
    class Meta:
        model = DetalleGasto
        fields = ['importe', 'concepto', 'tipo_gasto', 'concepto2', 'proveedor', 'comentarios']
        labels = {
            'concepto': 'Tipo de Movimiento',  # 👈 CAMBIO SOLO VISUAL
            'tipo_gasto': 'Forma de Pago',# 👈 CAMBIO SOLO VISUAL
            'concepto2': 'Cuenta',# 👈 CAMBIO SOLO VISUAL
        }
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'concepto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_gasto': forms.Select(attrs={'class': 'form-control'}),
            'concepto2': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre','fecha_evento','estatus']

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
        labels = {'concepto': 'Tipo de Movimiento',
                  'tipo_gasto': 'Forma de Pago',# 👈 CAMBIO SOLO VISUAL
                  'concepto2': 'Cuenta',# 👈 CAMBIO SOLO VISUAL

                 }
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'concepto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_gasto': forms.Select(attrs={'class': 'form-control'}),
            'concepto2': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
            }

class EstatusGastoForm(forms.ModelForm):
    class Meta:
        model = DetalleGasto
        fields = ['estatus']
        widgets = {
            'estatus': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'estatus': 'Estatus del gasto'
        }


class GastoFormConEvento(forms.ModelForm):

    class Meta:
        model = DetalleGasto
        fields = ['evento', 'importe', 'concepto', 'tipo_gasto', 'concepto2', 'proveedor', 'comentarios']
        labels = {
            'concepto': 'Tipo de Movimiento',
            'tipo_gasto': 'Forma de Pago',
            'concepto2': 'Cuenta',
        }
        widgets = {
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'concepto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_gasto': forms.Select(attrs={'class': 'form-control'}),
            'concepto2': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔥 Ordenar eventos alfabéticamente
        self.fields['evento'].queryset = Evento.objects.order_by('nombre')


class GraduadoForm(forms.ModelForm):

    class Meta:
        model = Graduado
        fields = '__all__'

