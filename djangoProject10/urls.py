"""
URL configuration for djangoProject10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Farmaciaa import views

urlpatterns = [
    # Ruta para el admin
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('producto/', views.producto, name='producto'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('inventario_sucursal/', views.inventario_sucursal, name='inventario_sucursal'),
    path('venta_medicamentos/', views.venta_medicamentos, name='venta_medicamentos'),
    path('transferencia_medicamentos/', views.transferencia_medicamentos, name='transferencia_medicamentos'),
    path('realizar_pedido/', views.realizar_pedido, name='realizar_pedido'),




]
