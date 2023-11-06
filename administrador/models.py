from django.db import models

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
    password = models.CharField(max_length=25)
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
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos_como_repartidor')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recojo = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    direccion = models.CharField(max_length=150)
    estado = models.BooleanField(default=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.cliente.correo
    class Meta:
        db_table = 'pedidos'
