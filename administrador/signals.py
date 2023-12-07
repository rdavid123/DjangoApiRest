from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role, Servicio

@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    # Verifica si la tabla de roles está vacía
    if Role.objects.count() == 0:
        # Crea los registros de roles predeterminados
        Role.objects.create(rol='ROLE_ADMIN', descripcion='Administrador de la pagina web')
        Role.objects.create(rol='ROLE_CLIENTE', descripcion='Usuario Normal de la pagina web')
        Role.objects.create(rol='ROLE_EMPLEADO', descripcion='realiza los servicios disponibles')
        Role.objects.create(rol='ROLE_REPARTIDOR', descripcion='reparte y recoje los pedidos')
        
