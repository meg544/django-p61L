"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.contrib import admin
from django.urls import path, include


from myapp.views import logout_view,generar_pdf_multiple,listar_gastos2,seleccionar_evento_listar_gastos2,seleccionar_evento_listar_gastos, seleccionar_evento, capturar_gastos, listar_gastos, generar_pdf, listar_eventos, crear_evento, editar_evento, eliminar_evento,listar_proveedores, crear_proveedor, editar_proveedor, eliminar_proveedor, reporte_pagos_proveedor
from django.contrib.auth import views as auth_views
urlpatterns = [path('admin/', admin.site.urls),

               #cambio 2 mayo 2025
               # Página de inicio personalizada
               #path('', seleccionar_evento, name='inicio'),

               # Página de login (acceso explícito)
               #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

               # Página de logout
               #path('logout/', logout_view, name='logout'),
               #aqui termina el cambio 2 mayo 2025

               #penultimo cambio
               path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # URL raíz para la página de inicio

               # Página de login
               path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

               # Página de logout
               path('logout/', logout_view, name='logout'),
                #fin penultimo cambio

    path('seleccionar-evento/', seleccionar_evento, name='seleccionar_evento'),
    path('capturar-gastos/<int:evento_id>/', capturar_gastos, name='capturar_gastos'),
    path('listar-gastos/<int:evento_id>/', listar_gastos, name='listar_gastos'),
    path('listar-gastos2/<int:evento_id>/', listar_gastos2, name='listar_gastos2'),
    path('pdf/<int:folio>/', generar_pdf, name='generar_pdf'),
    path('generar_pdf_multiple/', generar_pdf_multiple, name='generar_pdf_multiple'),

    #eventos
    path('eventos/', listar_eventos, name='listar_eventos'),
    path('eventos/crear/', crear_evento, name='crear_evento'),
    path('eventos/editar/<int:pk>/', editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', eliminar_evento, name='eliminar_evento'),
    #Proveedor
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),
    path('seleccionar-evento-listar-gastos/', seleccionar_evento_listar_gastos, name='seleccionar_evento_listar_gastos'),
    path('seleccionar-evento-listar-gastos2/', seleccionar_evento_listar_gastos2, name='seleccionar_evento_listar_gastos2'),
    path('reporte-pagos/', reporte_pagos_proveedor, name='reporte_pagos_proveedor'),
]


