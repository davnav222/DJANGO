from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),

    # --- SECCIONES ---
    path('secciones/', views.lista_secciones, name='lista_secciones'),
    path('secciones/alta/', views.alta_seccion, name='alta_seccion'),
    path('secciones/borrar/<int:id>/', views.borrar_seccion, name='borrar_seccion'),

    # --- CLIENTES ---
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/alta/', views.alta_cliente, name='alta_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # --- PRODUCTOS ---
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/alta/', views.alta_producto, name='alta_producto'),
    path('productos/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # --- VENTAS ---
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/alta/', views.alta_venta, name='alta_venta'),
    path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
    
#    path('configuracion/', views.configuracion, name='configuracion'),
]
