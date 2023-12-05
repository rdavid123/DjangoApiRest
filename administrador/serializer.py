from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer): # SOLO PARA POST, PUT, DELETE
    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer): # SOLO PARA GET !!
    rol = RoleSerializer()
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        rol_data = validated_data.pop('rol')
        role, created = Role.objects.get_or_create(**rol_data)
        user = User.objects.create(rol=role, **validated_data)
        return user


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class PedidoDetailSerializer(serializers.ModelSerializer): #Para GET
    cliente = UserDetailSerializer()
    repartidor = UserDetailSerializer()
    servicio = ServicioSerializer()
    class Meta:
        model = Pedido
        fields = '__all__'
        
class PedidoSerializer(serializers.ModelSerializer): #Para POST PUT y DELETE
    class Meta:
        model = Pedido
        fields = '__all__'
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = '__all__'