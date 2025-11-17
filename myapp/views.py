

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
from weasyprint import HTML
from myapp.models import Evento, DetalleGasto
from myapp.forms import DetalleGastoForm, EventoForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Proveedor
from .forms import EventoForm, ProveedorForm

from django.conf import settings
from django.contrib.staticfiles import finders


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
    gastos = DetalleGasto.objects.filter(evento=evento)
    total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0  # Calcula la suma de los importes
    return render(request, 'listar_gastos.html', {'gastos': gastos, 'evento': evento, 'total': total_importe,})

def listar_gastos2(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    gastos = DetalleGasto.objects.filter(evento=evento)
    total_importe = gastos.aggregate(total=Sum('importe'))['total'] or 0  # Calcula la suma de los importes
    return render(request, 'listar_gastos2.html', {'gastos': gastos, 'evento': evento, 'total': total_importe,})



def generar_pdf(request, folio):
    gasto = get_object_or_404(DetalleGasto, folio=folio)

    template_path = 'recibo_gasto.html'
    context = {
        'gasto': gasto,
        'icon': f"{settings.STATIC_URL}images/logo.jpg",
    }

    # Renderiza HTML
    template = get_template(template_path)
    html = template.render(context)

    # Función para convertir rutas estáticas (WeasyPrint requiere rutas absolutas)
    def fix_static_paths(content):
        static_prefix = settings.STATIC_URL
        while static_prefix in content:
            start = content.find(static_prefix)
            end = content.find('"', start)
            if end == -1:
                break
            static_path = content[start:end]
            real_path = finders.find(static_path.replace(static_prefix, ""))
            if real_path:
                content = content.replace(static_path, "file://" + real_path)
            else:
                break
        return content

    html = fix_static_paths(html)

    # Generar PDF
    pdf = HTML(string=html).write_pdf()

    # Respuesta HTTP
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

    template_path = 'recibo_gastos_multiples.html'
    context = {
        'gastos': gastos,
        'icon': f"{settings.STATIC_URL}images/logo.jpg",
    }

    # Renderiza HTML
    template = get_template(template_path)
    html = template.render(context)

    # Convertir rutas estáticas a absolutas para WeasyPrint
    def fix_static_paths(content):
        static_prefix = settings.STATIC_URL
        while static_prefix in content:
            start = content.find(static_prefix)
            end = content.find('"', start)
            if end == -1:
                break
            static_path = content[start:end]
            real_path = finders.find(static_path.replace(static_prefix, ""))
            if real_path:
                content = content.replace(static_path, "file://" + real_path)
            else:
                break
        return content

    html = fix_static_paths(html)

    # Generar PDF final
    pdf = HTML(string=html).write_pdf()

    # Respuesta HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recibo_gastos_multiples.pdf"'

    return response

