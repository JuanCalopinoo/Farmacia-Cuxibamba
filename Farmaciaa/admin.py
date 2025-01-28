# admin.py

from django.contrib import admin
from .models import Cliente, Empleado
from .models import Proveedor, Medicamento, Sucursal, Direccion, Farmacia,  InventarioSucursal
from .models import  Pedido, Registro, Entrega, Transferencia, OpcionEntregaModel
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Medicamento)
admin.site.register(Sucursal)
admin.site.register(Direccion)
admin.site.register(Farmacia)
admin.site.register(InventarioSucursal)
admin.site.register(Pedido)
admin.site.register(Registro)
admin.site.register(Entrega)
admin.site.register(Transferencia)
admin.site.register(OpcionEntregaModel)




