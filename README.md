# Farmacia-Cuxibamba by Juan Calopino
# Sistema de Gestión para una Cadena de Farmacias
![image](https://github.com/user-attachments/assets/b9fc00b3-f076-45be-893f-a6dbdf40c94f)

Este proyecto consiste en el desarrollo de un sistema para gestionar una cadena de farmacias con múltiples sucursales, utilizando el framework Django. El sistema permitirá la venta de medicamentos, la gestión de inventarios, transferencias entre sucursales y el seguimiento de pedidos.

---

## Características Principales

1. **Gestión de Inventario**:
   - Control del stock de medicamentos en cada sucursal.
   - Actualización automática del inventario tras cada venta o transferencia.

2. **Venta de Medicamentos**:
   - Permite realizar ventas de medicamentos disponibles en la sucursal.
   - En caso de falta de stock, se habilita la compra desde otra sucursal.

3. **Transferencias entre Sucursales**:
   - Proceso eficiente para solicitar medicamentos desde otra sucursal.
   - Registro y notificación automática de las transferencias realizadas.

4. **Opciones de Entrega**:
   - El cliente puede elegir entre:
     - Retirar el medicamento en la sucursal de origen.
     - Recibir el medicamento en la sucursal donde realizó la compra.

5. **Registro de Clientes y Pedidos**:
   - Sistema para almacenar información de clientes y sus pedidos.
   - Seguimiento del estado de cada pedido.

6. **Autenticación de Usuarios**:
   - Implementación de roles específicos:
     - **Administrador**: Control total del sistema.
     - **Empleado de Sucursal**: Gestión de ventas e inventarios locales.
     - **Cliente**: Acceso a su información de pedidos y opciones de compra.

---

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python 3.11
- **Framework Web**: Django 
- **Base de Datos**: Base de datos local de PyCharm  
- **Frontend**: HTML, CSS, JavaScript 

---

## Requisitos del Sistema

1. **Python**: Instalar la versión 3.8 o superior.
2. **Django**: Instalar mediante pip con `pip install django`.
3. **PostgreSQL**: Configurar una base de datos para el proyecto.
4. **Dependencias adicionales**:
   - Configuradas en el archivo `requirements.txt` del proyecto.

---

## Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone <URL del repositorio>
   cd <directorio del proyecto>
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la base de datos en el archivo `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_base_de_datos',
           'USER': 'usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': 5432'',
       }
   }
   ```

4. Realizar las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## Uso del Sistema

1. **Administrador**:
   - Acceso a la interfaz de administración para gestionar inventarios, sucursales y usuarios.

2. **Empleado de Sucursal**:
   - Gestión de ventas y transferencias desde el panel asignado.

3. **Cliente**:
   - Consultar el estado de sus pedidos y realizar compras.

---

## Objetivos del Sistema

- **Gestión eficiente** del inventario y las ventas en cada sucursal.
- **Optimizar la experiencia del cliente**, ofreciendo soluciones rápidas ante la falta de stock.
- **Centralizar la información** de las operaciones de la cadena de farmacias.

---

## Estructura del Repositorio
- `/`:
  - Imagene de diagrama de clases Uml
- `/`:
  - Contiene este archivo README.
  - Archivo `requirements.txt` para las dependencias.
- `/app`:
  - Código fuente del proyecto.

---



