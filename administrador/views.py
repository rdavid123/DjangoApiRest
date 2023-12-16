from rest_framework import viewsets
from . serializer import *
from . models import *

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
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

            # Verificar la contraseña encriptada
            if check_password(password, user.password):
                # Usuario autenticado correctamente, generar tokens JWT
                refresh = RefreshToken.for_user(user)
                user_serializer = UserSerializer(user)
                usuario_info = user_serializer.data
                #return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': usuario_info})
                return Response(usuario_info)
            else:
                # Contraseña incorrecta
                return Response({'detail': 'No active account found with the given credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            # Si la autenticación falla, devolver un mensaje de error
            return Response({'detail': 'No active account found with the given credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register_admin(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud
        data = request.data
        # Asegurarse de que la contraseña esté presente en los datos
        if 'password' not in data:
            return Response({'error': 'La contraseña es obligatoria.'}, status=status.HTTP_400_BAD_REQUEST)
        rol = Role.objects.get(id=1)
        # Crear una instancia del modelo User
        user = User(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            correo=data.get('correo'),
            telefono=data.get('telefono'),
            dni=data.get('dni'),
            avatar=None,
            rol=rol,
            estado_repartidor=data.get('estado_repartidor', True),  # Valor predeterminado a True si no está presente
            password=make_password(data['password'])  # Cifrar la contraseña usando make_password
        )
        # Guardar el usuario en la base de datos
        user.save()
        # Puedes devolver una respuesta de éxito u otros datos según tus necesidades
        return Response({'message': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud
        data = request.data
        # Asegurarse de que la contraseña esté presente en los datos
        if 'password' not in data:
            return Response({'error': 'La contraseña es obligatoria.'}, status=status.HTTP_400_BAD_REQUEST)
        rol = Role.objects.get(id=2)
        # Crear una instancia del modelo User
        user = User(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            correo=data.get('correo'),
            telefono=data.get('telefono'),
            dni=data.get('dni'),
            avatar=None,
            rol=rol,
            estado_repartidor=data.get('estado_repartidor', True),  # Valor predeterminado a True si no está presente
            password=make_password(data['password'])  # Cifrar la contraseña usando make_password
        )

        # Guardar el usuario en la base de datos
        user.save()
        # Puedes devolver una respuesta de éxito u otros datos según tus necesidades
        return Response({'message': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)
    
    
@api_view(['POST'])
def register_empleado(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud
        data = request.data
        # Asegurarse de que la contraseña esté presente en los datos
        if 'password' not in data:
            return Response({'error': 'La contraseña es obligatoria.'}, status=status.HTTP_400_BAD_REQUEST)
        rol = Role.objects.get(id=3)
        # Crear una instancia del modelo User
        user = User(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            correo=data.get('correo'),
            telefono=data.get('telefono'),
            dni=data.get('dni'),
            avatar=None,
            rol=rol,
            estado_repartidor=data.get('estado_repartidor', True),  # Valor predeterminado a True si no está presente
            password=make_password(data['password'])  # Cifrar la contraseña usando make_password
        )
        # Guardar el usuario en la base de datos
        user.save()
        # Puedes devolver una respuesta de éxito u otros datos según tus necesidades
        return Response({'message': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def register_repartidor(request):
    if request.method == 'POST':
        # Obtener datos del cuerpo de la solicitud
        data = request.data
        # Asegurarse de que la contraseña esté presente en los datos
        if 'password' not in data:
            return Response({'error': 'La contraseña es obligatoria.'}, status=status.HTTP_400_BAD_REQUEST)
        rol = Role.objects.get(id=4)
        # Crear una instancia del modelo User
        user = User(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            correo=data.get('correo'),
            telefono=data.get('telefono'),
            dni=data.get('dni'),
            avatar=None,
            rol=rol,
            estado_repartidor=data.get('estado_repartidor', True),  # Valor predeterminado a True si no está presente
            password=make_password(data['password'])  # Cifrar la contraseña usando make_password
        )
        # Guardar el usuario en la base de datos
        user.save()
        # Puedes devolver una respuesta de éxito u otros datos según tus necesidades
        return Response({'message': 'Repartidor registrado exitosamente.'}, status=status.HTTP_201_CREATED)


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
    
class PedidosByClienteView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        queryset = Pedido.objects.filter(cliente=cliente_id)
        return queryset