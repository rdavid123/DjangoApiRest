from rest_framework import viewsets
from . serializer import *
from . models import *

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener las credenciales del cuerpo de la solicitud
        correo = request.data.get('correo')
        password = request.data.get('password')
        print(f"Credenciales: correo={correo}, password={password}")
        try:
            # Buscar al usuario en tu modelo personalizado de Usuario
            user = User.objects.get(correo=correo)  # Utilizar el campo 'correo' de tu modelo
            print(f"Usuario encontrado: {user}")
            # Verificar la contraseña
            if user.password == password:
                # Usuario autenticado correctamente, generar tokens JWT
                refresh = RefreshToken.for_user(user)
                user_serializer = UserSerializer(user)
                usuario_info = user_serializer.data
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': usuario_info})
            else:
                # Contraseña incorrecta
                return Response({'detail': 'No active account found with the given credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            # Si la autenticación falla, devolver un mensaje de error
            return Response({'detail': 'No active account found with the given credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#Para actualizar la info. de un usuario
class UserViewUpdate(viewsets.ModelViewSet):
    serializer_class = UserSerializerForUpdate
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

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

class OfertasView(viewsets.ModelViewSet):
    queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer
    
class PagoView(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()

class PagoDetailView(viewsets.ModelViewSet):
    serializer_class = PagoDetailSerializer
    queryset = Pago.objects.all()