from django.urls import path, include
from rest_framework import routers
from . import views

#from . import views

router = routers.DefaultRouter()
router.register(r'roles',views.RoleView, 'roles')
router.register(r'users',views.UserView, 'users')
router.register(r'clientes',views.ClientesView, 'clientes')
router.register(r'empleados',views.EmpleadosView, 'empleados')
router.register(r'repartidores',views.RepartidoresView, 'repartidores')
router.register(r'users_detail',views.UserDetailView, 'usersdetail')
router.register(r'servicios',views.ServicioView, 'servicios')
router.register(r'pedidos',views.PedidoView, 'pedidos')
router.register(r'pedidosdetail',views.PedidoDetailView, 'pedidosdetail')
router.register(r'productos', views.ProductoViewSet, 'productos')
router.register(r'Ofertas', views.OfertasView, 'Ofertas')

urlpatterns = [
    path('', include(router.urls)),
    path('users/email/<str:correo>/', views.users_by_email),
]
