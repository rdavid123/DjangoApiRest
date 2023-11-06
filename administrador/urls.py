from django.urls import path, include
from rest_framework import routers
from . import views

#from . import views

router = routers.DefaultRouter()
router.register(r'roles',views.RoleView, 'roles')
router.register(r'users',views.UserView, 'users')
router.register(r'servicios',views.ServicioView, 'servicios')
router.register(r'pedidos',views.PedidoView, 'pedidos')

urlpatterns = [
    path('', include(router.urls)),
]