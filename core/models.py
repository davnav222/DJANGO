from django.db import models

# 1. SECCIONES (Categorías de productos)
class Seccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 2. CLIENTES
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 3. PRODUCTOS (Relacionados con una Sección)
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.stock} uds)"

# 4. VENTAS (Relacionan un Cliente y un Producto)
class Venta(models.Model):
    codigo = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField(default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.codigo} - {self.cliente.nombre}"

class Configuracion(models.Model):
    nombre_empresa = models.CharField(max_length=150, default="Mi Empresa S.A.")
    cif = models.CharField(max_length=20, default="A12345678B")
    direccion = models.CharField(max_length=255, default="Calle Principal, 1")
    iva_general = models.DecimalField(max_digits=5, decimal_places=2, default=21.0)

    def __str__(self):
        return self.nombre_empresa
        

