#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('footer', views.footer, name='footer'),
    path('navbar', views.navbar, name='navbar'),
    path('mantencion', views.mantencion, name='mantencion'),
    path('reparacion', views.reparacion, name='reparacion'),
    path('refacciones', views.refacciones, name='refacciones'),
    path('crud', views.crud, name='crud'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
]