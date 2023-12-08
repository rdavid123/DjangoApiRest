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

class UserDetailView(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    
class ClientesView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(rol=2)
    
class EmpleadosView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(rol=3)

class RepartidoresView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(rol=4)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def users_by_email(request, correo):    
    user = User.objects.filter(correo=correo).first()
    if request.method == 'GET':
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class ServicioView(viewsets.ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()

class PedidoDetailView(viewsets.ModelViewSet):
    serializer_class = PedidoDetailSerializer
    queryset = Pedido.objects.all()
    
class PedidoView(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class OfertasView(viewsets.ModelViewSet):
    queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer
    
class PagoView(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()

class PagoDetailView(viewsets.ModelViewSet):
    serializer_class = PagoDetailSerializer
    queryset = Pago.objects.all()