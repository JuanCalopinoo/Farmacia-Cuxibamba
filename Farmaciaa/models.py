from django.db import models



class EstadoPedido(models.TextChoices):
    ENTREGADO = "ENTREGADO", "Entregado"
    CANCELADO = "CANCELADO", "Cancelado"
    EN_PROCESO = "EN_PROCESO", "En proceso"



class OpcionEntrega(models.TextChoices):
    RETIRO_EN_SUCURSAL = "RETIRO_EN_SUCURSAL", "Retiro en Sucursal"
    ENVIO_DESDE_ORIGEN = "ENVIO_DESDE_ORIGEN", "Envío desde Sucursal de Origen"


class OpcionEntregaModel(models.Model):
    opcion = models.CharField(max_length=20, choices=OpcionEntrega.choices)

    def __str__(self):
        return self.get_opcion_display()



class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Cliente(Persona):
    es_frecuente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class Empleado(Persona):
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rol}"


class Proveedor(models.Model):
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.contacto


# Direcciones y farmacias
class Direccion(models.Model):
    calle_principal = models.CharField(max_length=255)
    calle_secundaria = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.calle_principal} y {self.calle_secundaria}, {self.ciudad}"


class Farmacia(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    # Método para listar los medicamentos disponibles en la farmacia
    def listar_medicamentos(self):
        inventarios = InventarioSucursal.objects.filter(sucursal=self)
        return [inventario.medicamento.nombre for inventario in inventarios]



class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    # Método para actualizar el precio de un medicamento
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
            self.save()
        else:
            raise ValueError("El precio no puede ser negativo")


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    # Método para calcular el total del inventario
    def total_inventario(self):
        inventarios = InventarioSucursal.objects.filter(sucursal=self)
        return sum([inventario.cantidad for inventario in inventarios])


class InventarioSucursal(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="inventarios")
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.medicamento.nombre} en {self.sucursal.nombre}: {self.cantidad} unidades"

    # Método para actualizar el inventario
    def actualizar_inventario(self, cantidad_nueva):
        if cantidad_nueva >= 0:
            self.cantidad = cantidad_nueva
            self.save()
        else:
            raise ValueError("La cantidad no puede ser negativa")

    # Método para verificar la disponibilidad de un medicamento en una sucursal
    def disponibilidad_en_sucursal(self, sucursal):
        inventario = InventarioSucursal.objects.filter(medicamento=self.medicamento, sucursal=sucursal).first()
        return inventario.cantidad if inventario else 0



class Pedido(models.Model):
    detalle_pedido = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    sucursal_entrega = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="pedidos_entrega", null=True,
                                         blank=True)
    opcion_entrega = models.CharField(
        max_length=20, choices=OpcionEntrega.choices, default=OpcionEntrega.RETIRO_EN_SUCURSAL
    )
    estado = models.CharField(max_length=20, choices=EstadoPedido.choices, default=EstadoPedido.EN_PROCESO)

    def __str__(self):
        return f"Pedido: {self.detalle_pedido} - {self.estado} - {self.get_opcion_entrega_display()}"

    # Método para actualizar el estado del pedido
    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado in dict(EstadoPedido.choices):
            self.estado = nuevo_estado
            self.save()
        else:
            raise ValueError("Estado no válido")

    # Método para obtener el detalle de entrega
    def get_detalle_entrega(self):
        return f"Pedido {self.id} - Estado: {self.get_estado_display()} - Entregado: {self.opcion_entrega}"



class Entrega(models.Model):
    tipo_entrega = models.CharField(max_length=100)
    fecha_entrega = models.DateTimeField()
    estado_entrega = models.CharField(max_length=100)
    se_pudo_entregar = models.BooleanField(default=False)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name="entrega", null=True, blank=True)

    def __str__(self):
        return f"Entrega {self.estado_entrega} - {self.fecha_entrega}"

    # Método para marcar la entrega como completada
    def marcar_entregado(self):
        self.estado_entrega = "Entregado"
        self.se_pudo_entregar = True
        self.save()

    # Método para obtener la fecha de entrega en un formato legible
    def get_fecha_entrega_formato(self):
        return self.fecha_entrega.strftime('%d/%m/%Y %H:%M:%S')



class Transferencia(models.Model):
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="transferencias_salida")
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="transferencias_entrada")
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transferencia de {self.cantidad} {self.medicamento.nombre} de {self.sucursal_origen} a {self.sucursal_destino}"


    def realizar_transferencia(self):
        if self.sucursal_origen != self.sucursal_destino:
            inventario_origen = InventarioSucursal.objects.get(sucursal=self.sucursal_origen,
                                                               medicamento=self.medicamento)
            inventario_destino = InventarioSucursal.objects.get(sucursal=self.sucursal_destino,
                                                                medicamento=self.medicamento)

            # Restamos de la sucursal origen
            inventario_origen.actualizar_inventario(inventario_origen.cantidad - self.cantidad)

            # Sumamos a la sucursal destino
            inventario_destino.actualizar_inventario(inventario_destino.cantidad + self.cantidad)

            # Guardamos la transferencia
            self.save()
        else:
            raise ValueError("Las sucursales de origen y destino deben ser diferentes")


# Registro de actividades
class Registro(models.Model):
    pedidos = models.ManyToManyField(Pedido)
    clientes = models.ManyToManyField(Cliente)

    def __str__(self):
        return f"Registro con {len(self.pedidos.all())} pedidos y {len(self.clientes.all())} clientes"

    # Método para agregar un pedido al registro
    def agregar_pedido(self, pedido):
        self.pedidos.add(pedido)
        self.save()
