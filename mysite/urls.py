from django.contrib import admin
from django.urls import path
from myapp.views import (
    seleccionar_proveedor, listar_gastos_proveedor,
    logout_view,
    generar_pdf_multiple,
    listar_gastos2,
    seleccionar_evento_listar_gastos2, seleccionar_evento_listar_gastos,
    seleccionar_evento, capturar_gastos, listar_gastos,
    generar_pdf,
    listar_eventos, crear_evento, editar_evento,
    eliminar_evento, listar_proveedores, crear_proveedor,
    editar_proveedor, eliminar_proveedor, reporte_pagos_proveedor, editar_gasto,
    listar_conceptos, editar_concepto,eliminar_concepto, crear_concepto,
    listar_categorias,editar_categoria,eliminar_categoria,crear_categoria,
    gastos_lista,gasto_crear,gasto_editar,gasto_eliminar,sin_permiso,
    generar_pdf_multiple3,
    gastos_lista3,
    seleccionar_evento1,capturar_gastos1,listar_gastos1,
    generar_pdf_multiple2,
    gastos_estatus_lista,cambiar_estatus_rapido,seleccionar_evento_estatus,
    editar_gasto_evento,
    gastos_estatus_lista2,cambiar_estatus_rapido2,seleccionar_evento_estatus2,
    seleccionar_prov2, listar_gtos_prov2,

)
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('admin/', admin.site.urls),

    # Login & Logout
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    # EVENTOS
    path('seleccionar-evento/', seleccionar_evento, name='seleccionar_evento'),
    path('capturar-gastos/<int:evento_id>/', capturar_gastos, name='capturar_gastos'),
    path('listar-gastos/<int:evento_id>/', listar_gastos, name='listar_gastos'),
    path('listar-gastos2/<int:evento_id>/', listar_gastos2, name='listar_gastos2'),
    path('pdf/<int:folio>/', generar_pdf, name='generar_pdf'),
    path('generar_pdf_multiple/', generar_pdf_multiple, name='generar_pdf_multiple'),

    # CRUD EVENTOS
    path('eventos/', listar_eventos, name='listar_eventos'),
    path('eventos/crear/', crear_evento, name='crear_evento'),
    path('eventos/editar/<int:pk>/', editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', eliminar_evento, name='eliminar_evento'),

    # CRUD PROVEEDORES
    path('proveedores/listar/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),

    # REPORTES POR PROVEEDOR

    # nuevas rutas para editar e imprimir gastos
    path("gasto/<int:pk>/editar/", editar_gasto, name="editar_gasto"),


    # Reporte con fechas
    path('reporte_pagos_proveedor/', reporte_pagos_proveedor, name='reporte_pagos_proveedor'),
    path("seleccionar-proveedor/", seleccionar_proveedor, name="seleccionar_proveedor"),
    path("proveedor/<int:proveedor_id>/gastos/", listar_gastos_proveedor, name="listar_gastos_proveedor"),

    # Selecciones extra
    path('seleccionar-evento-listar-gastos/', seleccionar_evento_listar_gastos, name='seleccionar_evento_listar_gastos'),
    path("gasto-evento/editar/<int:folio>/", editar_gasto_evento, name="editar_gasto_evento"),
    path('seleccionar-evento-listar-gastos2/', seleccionar_evento_listar_gastos2, name='seleccionar_evento_listar_gastos2'),

    # Categorías
    path("categorias/", listar_categorias, name="listar_categorias"),
    path("categorias/crear/", crear_categoria, name="crear_categoria"),
    path("categorias/editar/<int:pk>/", editar_categoria, name="editar_categoria"),
    path("categorias/eliminar/<int:pk>/", eliminar_categoria, name="eliminar_categoria"),

    # Conceptos
    path("conceptos/", listar_conceptos, name="listar_conceptos"),
    path("conceptos/crear/", crear_concepto, name="crear_concepto"),
    path("conceptos/editar/<int:pk>/", editar_concepto, name="editar_concepto"),
    path("conceptos/eliminar/<int:pk>/", eliminar_concepto, name="eliminar_concepto"),

    # Nuevas rutas de gastos
    path('ogastos/', gastos_lista, name='gastos_lista'),
    path('ogastos/nuevo/', gasto_crear, name='gasto_crear'),
    path('ogastos/editar/<int:folio>/', gasto_editar, name='gasto_editar'),
    path('ogastos/eliminar/<int:folio>/', gasto_eliminar, name='gasto_eliminar'),
    path('generar_pdf_multiple3/', generar_pdf_multiple3, name='generar_pdf_multiple3'),
    path('generar_pdf_multiple2/', generar_pdf_multiple2, name='generar_pdf_multiple2'),
    path('ogastos/lista3', gastos_lista3, name='gastos_lista3'),
    #sin permiso
    path('sin_permiso/', sin_permiso, name='sin_permiso'),

    # Captura de gastos New
    path('seleccionar-evento1/', seleccionar_evento1, name='seleccionar_evento1'),
    path('capturar-gastos1/<int:evento_id>/', capturar_gastos1, name='capturar_gastos1'),
    path('listar-gastos1/<int:evento_id>/', listar_gastos1, name='listar_gastos1'),

    path('estatus/<int:evento_id>/', gastos_estatus_lista, name="gastos_estatus_lista"),
    path('estatus/cambiar/<int:folio>/', cambiar_estatus_rapido, name="cambiar_estatus_rapido"),
    path('seleccionar-evento-estatus/', seleccionar_evento_estatus, name='seleccionar_evento_estatus'),

    #estatus version 2
    path('estatus2/<int:evento_id>/', gastos_estatus_lista2, name="gastos_estatus_lista2"),
    path('estatus2/cambiar2/<int:folio>/', cambiar_estatus_rapido2, name="cambiar_estatus_rapido2"),
    path('estatus2/seleccionar-evento-estatus2/', seleccionar_evento_estatus2, name='seleccionar_evento_estatus2'),

    #se adiciona seleccionar proveedor 2
    path("seleccionar-prov2/", seleccionar_prov2, name="seleccionar_prov2"),
    path("prov2/<int:proveedor_id>/gastos/", listar_gtos_prov2, name="listar_gtos_prov2"),

]
