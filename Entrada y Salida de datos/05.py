"""
Calcular el precio neto de un producto. El nombre del producto y su precio con IVA
(19%) deben ser ingresados por el usuario. El resultado debe ser mostrado por
pantalla:
El precio neto de [PRODUCTO] es $[PRECIO_NETO]
"""

nombre = input("Producto: ")
precio = int(input("Precio: "))

iva = precio * 0.19
precio_neto = precio - iva

print(f"El precio neto de {nombre} es ${precio_neto:.0f}")
