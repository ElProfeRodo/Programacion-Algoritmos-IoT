"""
Calcular la propina (10%) por un pedido en un restaurante. Debe solicitar el nombre
de 3 productos, el precio unitario de cada uno y las cantidades solicitadas.
Mostrar por pantalla el siguiente detalle:
2 x completo       $2.000
3 x bebidas        $1.100
1 x postre         $1.500
Total del pedido   $8.800
Total con propina  $9.680
"""

producto1 = input("Producto 1: ")
precio1 = int(input("Precio 1: "))
cantidad1 = int(input("Cantidad 1:"))

producto2 = input("Producto 2: ")
precio2 = int(input("Precio 2: "))
cantidad2 = int(input("Cantidad 2:"))

producto3 = input("Producto 3: ")
precio3 = int(input("Precio 3: "))
cantidad3 = int(input("Cantidad 3:"))

subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3

total_pedido = subtotal1 + subtotal2 + subtotal3
total_con_propina = total_pedido * 1.10

print(f"{cantidad1} x {producto1} \t\t ${subtotal1}")
print(f"{cantidad2} x {producto2} \t\t ${subtotal2}")
print(f"{cantidad3} x {producto3} \t\t ${subtotal3}")
print(f"Total pedido \t\t ${total_pedido}")
print(f"Total con propina \t ${total_con_propina}")
