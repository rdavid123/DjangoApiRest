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
    avatar = models.ImageField(upload_to='imagenes/', null=True,default="imagenes/profile.jpg")
    password = models.CharField(max_length=100)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)
    estado_repartidor = models.BooleanField(default=True, null=True, blank=True)
    def __str__(self):
        return self.correo
    class Meta:
        db_table = 'users'

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True)
    def __str__(self):
        return self.titulo
    class Meta:
        db_table = 'servicios'

class Pedido(models.Model):
    OPCIONES_ENTREGA = [
        ('1', 'Recojo y envio a domicilio'),
        ('2', 'Recojo a Domicilio'),
    ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos_como_cliente')
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='pedidos_como_repartidor',null=True,blank=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    direccion = models.CharField(max_length=150)
    estado = models.CharField(max_length=20, 
        choices=[
            ('pendiente', 'Pendiente'), 
            ('proceso', 'En Proceso'), 
            ('proceso_terminado', 'Proceso Terminado'), 
            ('en_camino', 'En camino'),
            ('finalizado', 'Finalizado'),
            ('cancelado', 'Cancelado')
        ], default='pendiente')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad_prendas = models.IntegerField()
    tipo_entrega = models.CharField(max_length=10,choices=OPCIONES_ENTREGA,default='1')
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.cliente.correo} - {self.id}"
    class Meta:
        db_table = 'pedidos'
        
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    class Meta:
        db_table = 'Producto'

class Ofertas(models.Model):
    place_image = models.ImageField(upload_to='Ofertas/')
    titulo = models.CharField(max_length=255)
    Descripcion = models.TextField()
    articleDateTime = models.CharField(max_length=255)
    precio = models.FloatField()
    class Meta:
        db_table = 'Ofertas'
        
class Pago(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    transaccion_id = models.CharField(max_length=255)
    class Meta:
        db_table = 'Pagos'