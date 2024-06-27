#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('footer', views.footer, name='footer'),
    path('navbar', views.navbar, name='navbar'),
    path('mantencion', views.mantencion, name='mantencion'),
    path('reparacion', views.reparacion, name='reparacion'),
    path('refacciones', views.refacciones, name='refacciones'),
    path('trabajos', views.trabajos, name='trabajos'),
    path('contacto', views.contacto, name='contacto'),
    path('equipo', views.equipo, name='equipo'),
    path('nuevologin', views.nuevologin, name='nuevologin'),

    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('tienda/', views.lista_productos, name='lista_productos'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
]