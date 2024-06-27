from django.db import models

# Create your models here.

class Producto(models.Model):
    pro_id = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(unique=True, max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito {self.id}'

    def get_subtotal(self):
        return sum(item.get_total_precio() for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
    
    def get_total_precio(self):
        return self.cantidad * self.producto.precio