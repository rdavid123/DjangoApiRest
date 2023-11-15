from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.hashers import BCryptPasswordHasher

# Create your models here.
class Role(models.Model):
    rol = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.rol
    class Meta:
        db_table = 'roles'

class User(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=9)
    dni = models.CharField(max_length=8)
    avatar = models.ImageField(upload_to='imagenes/',default='imagenes/default.jpg')
    password = models.CharField(max_length=100)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.correo
    class Meta:
        db_table = 'users'

class Servicio(models.Model):
    servicio = models.CharField(max_length=25)
    def __str__(self):
        return self.servicio
    class Meta:
        db_table = 'servicios'

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos_como_cliente')
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos_como_repartidor',null=True, blank=True)
    fecha_pedido = models.DateTimeField()
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    direccion = models.CharField(max_length=150)
    estado = models.CharField(max_length=20, 
        choices=[
            ('pendiente', 'Pendiente'), 
            ('en_proceso', 'En Proceso'), 
            ('entregado', 'Entregado'),
            ('cancelado', 'Cancelado')
        ], default='pendiente')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.cliente.correo} - {self.id}"
    class Meta:
        db_table = 'pedidos'
