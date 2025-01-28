from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from Farmaciaa.models import Pedido, Sucursal, InventarioSucursal , Transferencia, Medicamento, Pedido, OpcionEntregaModel


def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def producto(request):
    return render(request, 'producto.html')
def lista_pedidos(request):
    pedidos = Pedido.objects.all()  # Obtiene todos los pedidos
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})



def inventario_sucursal(request):
    # Obtiene todos los registros de InventarioSucursal
    inventarios = InventarioSucursal.objects.all()
    return render(request, 'inventario_sucursal.html', {'inventarios': inventarios})
def venta_medicamentos(request):
    # Obtener todos los medicamentos disponibles en todas las sucursales
    medicamentos = Medicamento.objects.all()
    return render(request, 'venta_medicamentos.html', {'medicamentos': medicamentos})



def transferencia_medicamentos(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        sucursal_origen_id = request.POST.get('sucursal_origen')
        sucursal_destino_id = request.POST.get('sucursal_destino')
        medicamento_id = request.POST.get('medicamento')
        cantidad = int(request.POST.get('cantidad'))

        sucursal_origen = Sucursal.objects.get(id=sucursal_origen_id)
        sucursal_destino = Sucursal.objects.get(id=sucursal_destino_id)
        medicamento = Medicamento.objects.get(id=medicamento_id)

        # Verificar si hay suficiente stock en la sucursal origen
        inventario_origen = sucursal_origen.inventarios.filter(medicamento=medicamento).first()
        if inventario_origen and inventario_origen.cantidad >= cantidad:
            # Realizar la transferencia
            transferencia = Transferencia(
                sucursal_origen=sucursal_origen,
                sucursal_destino=sucursal_destino,
                medicamento=medicamento,
                cantidad=cantidad
            )
            transferencia.realizar_transferencia()
            messages.success(request, "Transferencia realizada con éxito.")
            return redirect('transferencia_medicamentos')
        else:
            messages.error(request, "No hay suficiente stock en la sucursal de origen.")

    # Obtener los medicamentos y las sucursales disponibles
    medicamentos = Medicamento.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'transferencia_medicamentos.html', {'medicamentos': medicamentos, 'sucursales': sucursales})






def realizar_pedido(request):
    if request.method == "POST":
        # Datos del pedido
        medicamento_id = request.POST.get('medicamento')
        cantidad = int(request.POST.get('cantidad'))
        opcion_entrega = request.POST.get('opcion_entrega')

        medicamento = Medicamento.objects.get(id=medicamento_id)

        # Crear pedido
        pedido = Pedido.objects.create(
            medicamento=medicamento,
            cantidad=cantidad,
            opcion_entrega=opcion_entrega
        )

        return render(request, 'pedido_confirmado.html', {'pedido': pedido})

    # Mostrar medicamentos y opciones de entrega
    medicamentos = Medicamento.objects.all()
    opciones_entrega = OpcionEntregaModel.objects.all()
    return render(request, 'realizar_pedido.html', {'medicamentos': medicamentos, 'opciones_entrega': opciones_entrega})
    # views.py

