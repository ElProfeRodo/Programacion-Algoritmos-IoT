"""
Escribe un programa que pida al usuario el precio de un producto y 
un porcentaje de descuento. El programa debe verificar que el descuento 
sea un valor válido (entre 0 y 100). Si el valor es válido, debe calcular
y mostrar el precio final con el descuento aplicado. Si no lo es, debe 
mostrar un mensaje de error.
"""

precio = int(input("Precio: "))
porcentaje = int(input("Porcentaje: "))

if porcentaje >= 0 and porcentaje <= 100:
    precio_final = precio - (precio * (porcentaje/100))
    print(f"El precio final es {precio_final}")
else:
    print("El porcentaje debe estar entre 0 y 100")