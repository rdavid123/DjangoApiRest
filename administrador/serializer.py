from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
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

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'