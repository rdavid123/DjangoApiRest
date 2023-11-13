from rest_framework import viewsets
from . serializer import *
from . models import *

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def users_by_email(request, correo):    
    user = User.objects.filter(correo=correo).first()
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ServicioView(viewsets.ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()

class PedidoView(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()