

# Create your models here.


from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from decimal import Decimal

class Evento(models.Model):
    ESTATUS_CHOICES = [
        ("abierto", "Abierto"),
        ("cerrado", "Cerrado"),
        ("cancelado", "Cancelado"),
    ]

    nombre = models.CharField(max_length=200, unique=True)
    estatus = models.CharField(
        max_length=10,
        choices=ESTATUS_CHOICES,
        default="abierto"
    )

    def __str__(self):
        return self.nombre



class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']  # Ordenar los proveedores en orden ascendente por nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Concepto(models.Model):
    concepto = models.CharField(max_length=200)
    estatus = models.BooleanField(default=True)  # Activo / Inactivo
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.concepto


class DetalleGasto(models.Model):
    folio = models.AutoField(primary_key=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=now, editable=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=200, choices=[
        ('pago', 'Pago'),
        ('anticipo', 'Anticipo'),
        ('prestamo', 'Prestamo'),
        ('adeudo', 'Adeudo'),
        ('apertura', 'Apertura Cta'),
        ('devolucion', 'Devolucion')
    ], default='pago')
    tipo_gasto = models.CharField(max_length=100, choices=[
        ('efe', 'Efectivo'),
        ('tdp', 'Transf. Directa Platinum'),
        ('puente', 'Transf. Puente'),
        ('deposito', 'Deposito a Proveedor'),
        ('caja', 'Caja Chica'),
        ('boveda', 'Boveda')
    ], default='efe')
    concepto2 = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)

    # 👇 NUEVO CAMPO
    estatus = models.CharField(
        max_length=10,
        choices=[
            ('ok', 'OK'),
            ('not_ok', 'Not OK')
        ],
        default='ok'
    )
    def __str__(self):
        return f"Folio {self.folio} - {self.evento.nombre}"

# models.py Ingresos

from django.core.validators import RegexValidator

class Graduado(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(r'^\+?\d{7,15}$', "Formato de teléfono inválido")
        ]
    )
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ConceptoIngresos(models.Model):
    ESTATUS_CHOICES = (
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    )

    concepto = models.CharField(max_length=200, unique=True)
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default="ACTIVO")

    def __str__(self):
        return self.concepto

class DetalleIngresos(models.Model):

    # Folio único y autoincremental
    folio = models.AutoField(primary_key=True)

    # Fecha automática al crear el registro
    fecha = models.DateTimeField(auto_now_add=True)

    # Importe validado como positivo
    importe = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )

    # Forma de pago
    forma_pago = models.CharField(max_length=100, choices=[
        ("EF", "Efectivo"),
        ("TR", "Transferencia"),
        ("MP", "Mercado Pago"),
        ("DS", "Depósito en sucursal"),
        ("PL", "Pago en línea"),
    ], default='efe')

    # Relaciones
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    concepto = models.ForeignKey(ConceptoIngresos, on_delete=models.CASCADE)
    graduado = models.ForeignKey(Graduado, on_delete=models.CASCADE)

    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ingreso #{self.folio} - {self.evento.nombre}"


