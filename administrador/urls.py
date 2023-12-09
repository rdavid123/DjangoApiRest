from django.urls import path, include
from rest_framework import routers
from . import views

#from . import views

router = routers.DefaultRouter()
router.register(r'roles',views.RoleView, 'roles')
#usuarios
router.register(r'users',views.UserView, 'users')
router.register(r'users_detail',views.UserDetailView, 'usersdetail')
router.register(r'usersupdate',views.UserViewUpdate, 'usersupdate')
router.register(r'clientes',views.ClientesView, 'clientes')
router.register(r'empleados',views.EmpleadosView, 'empleados')
router.register(r'repartidores',views.RepartidoresView, 'repartidores')
#servicios
router.register(r'servicios',views.ServicioView, 'servicios')
#pedidos
router.register(r'pedidos',views.PedidoView, 'pedidos')
router.register(r'pedidosdetail',views.PedidoDetailView, 'pedidosdetail')
router.register(r'Ofertas', views.OfertasView, 'Ofertas')
#pagos
router.register(r'pagos', views.PagoView, 'pagos')
router.register(r'pagosdetail', views.PagoDetailView, 'pagosdetail')

urlpatterns = [
    path('', include(router.urls)),
    path('users/email/<str:correo>/', views.users_by_email),
]
