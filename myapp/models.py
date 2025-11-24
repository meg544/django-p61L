

# Create your models here.


from django.db import models
from django.utils.timezone import now

class Evento(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

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
    concepto2 = models.ForeignKey(Concepto, on_delete=models.CASCADE, default=215)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Folio {self.folio} - {self.evento.nombre}"

# models.py






