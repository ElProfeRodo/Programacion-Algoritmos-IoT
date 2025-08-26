"""
Crear un programa que solicite el nombre y precio de un producto, junto con el
porcentaje de descuento que se le va a aplicar. El valor del precio puede ser un
número real y el valor del descuento debe ser un número entero.
Mostrar el nombre, el precio original y el precio con descuento por pantalla.
"""

producto = input("Producto: ")
precio = int(input("Precio: "))
porc_descuento = int(input("Descuento: "))

precio_descto = precio - (precio*porc_descuento/100)

print(f"{producto} costaba {precio}, ahora cuesta {precio_descto}")
