from numpy.ma.core import product
from sympy import false

print("***Sistema de Tienda Online***")

producto = "Cámara digital"
precio = 399.99
cantidad_inventario =20
esta_disponible = True

print("Producto:", producto)
print("Precio: $", precio)
print("Cantidad en inventario:", cantidad_inventario)
print("Disponible:", esta_disponible)

producto = "Laptop"
precio = 10000.00
cantidad_inventario = 10
esta_disponible = False
print()
print("Producto:", producto)
print("Precio: $", precio)
print("Cantidad en inventario:", cantidad_inventario)
print("Disponible:", esta_disponible)
