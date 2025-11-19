

# Create your views here.
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout

def logout_view(request):
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
        logout(request)
        return render(request, 'logout.html', {})


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Sum
from django.contrib.staticfiles import finders
from weasyprint import HTML, CSS

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Proveedor, DetalleGasto
from .forms import EventoForm, ProveedorForm, ReportePagosForm, DetalleGastoForm


from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

def abs_static(path):
    real_path = finders.find(path)
    if real_path:
        return "file://" + real_path
    return ""

def seleccionar_evento(request):
    eventos = Evento.objects.all().order_by('nombre')
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        return redirect('capturar_gastos', evento_id=evento_id)
    return render(request, 'seleccionar_evento.html', {'eventos': eventos})

def capturar_gastos(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = DetalleGastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.evento = evento
            gasto.save()
            return redirect('listar_gastos', evento_id=evento_id)
    else:
        form = DetalleGastoForm()
    return render(request, 'capturar_gastos.html', {'form': form, 'evento': evento})

def seleccionar_evento_listar_gastos(request):
    eventos = Evento.objects.all().order_by('nombre')
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        return redirect('listar_gastos', evento_id=evento_id)
    return render(request, 'seleccionar_evento.html', {'eventos': eventos})

def seleccionar_evento_listar_gastos2(request):
    eventos = Evento.objects.all().order_by('nombre')
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        return redirect('listar_gastos2', evento_id=evento_id)
    return render(request, 'seleccionar_evento.html', {'eventos': eventos})

def listar_gastos(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    gastos = DetalleGasto.objects.filter(evento=evento).order_by('-fecha')
    total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0  # Calcula la suma de los importes
    return render(request, 'listar_gastos.html', {'gastos': gastos, 'evento': evento, 'total': total_importe,})

def listar_gastos2(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    gastos = DetalleGasto.objects.filter(evento=evento).order_by('-fecha')
    total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0  # Calcula la suma de los importes
    return render(request, 'listar_gastos2.html', {'gastos': gastos, 'evento': evento, 'total': total_importe,})



def generar_pdf(request, folio):

    gasto = get_object_or_404(DetalleGasto, folio=folio)

    template_path = 'recibo_gasto.html'
    template = get_template(template_path)

    context = {
        'gasto': gasto,
        'icon': os.path.join(settings.STATIC_ROOT, "images/logo.jpg"),
    }

    html = template.render(context)

    pdf = HTML(
        string=html,
        base_url=request.build_absolute_uri('/')   # NECESARIO
    ).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="recibo_{folio}.pdf"'

    return response
# views.py


# Listar eventos
def listar_eventos(request):
    eventos = Evento.objects.all().order_by('nombre')
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

# Crear evento
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

# Editar evento
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form})

# Eliminar evento
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

# Proveedor
# views.py


# Listar proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    return render(request, 'proveedores/listar_proveedores.html', {'proveedores': proveedores})

# Crear proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/crear_proveedor.html', {'form': form})

# Editar proveedor
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/editar_proveedor.html', {'form': form})

# Eliminar proveedor
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'proveedores/eliminar_proveedor.html', {'proveedor': proveedor})



def generar_pdf_multiple(request):
    folios = request.GET.get('folios')
    if not folios:
        return HttpResponse("No se han seleccionado registros.", content_type="text/plain")

    folios = folios.split(',')
    gastos = DetalleGasto.objects.filter(folio__in=folios)

    template_path = "recibo_gastos_multiples.html"
    template = get_template(template_path)

    icon_path = abs_static("images/logo.jpg")   # ← ESTA ES LA CLAVE

    context = {
        "gastos": gastos,
        "icon": icon_path,
    }

    html = template.render(context)

    pdf = HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recibos.pdf"'

    return response






def reporte_pagos_proveedor(request):
    form = ReportePagosForm(request.GET or None)

    gastos = []
    total_importe = 0

    if form.is_valid():
        proveedor = form.cleaned_data['proveedor']
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']

        gastos = DetalleGasto.objects.filter(
            proveedor=proveedor,
            fecha__date__gte=fecha_inicio,
            fecha__date__lte=fecha_fin
        ).order_by('-fecha')

        total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0

    context = {
        'form': form,
        'gastos': gastos,
        'total_importe': total_importe,
    }
    return render(request, "reporte_pagos_proveedor.html", context)

def seleccionar_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        return redirect('listar_gastos_proveedor', proveedor_id=proveedor_id)
    return render(request, 'seleccionar_proveedor.html', {'proveedores': proveedores})

# views.py
def listar_gastos_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    gastos = DetalleGasto.objects.filter(
        proveedor=proveedor
    ).order_by("-fecha")  # DESC

    total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0

    context = {
        "proveedor": proveedor,
        "gastos": gastos,
        "total": total_importe,
    }

    return render(request, "listar_gastos_proveedor.html", context)
