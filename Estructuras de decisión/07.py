"""
Crear un programa que permita imprimir una boleta con el 
detalle de una compra. El programa debe solicitar tres 
productos y sus cantidades. Los precios de los productos 
deben ser definidos en el programa. El programa debe aplicar 
un descuento del 10% si la compra es igual o superior a 
$20.000, el detalle de la boleta se muestra por pantalla
"""
prec1 = 980
prec2 = 995
prec3 = 7995

# Se ingresan los productos
prod1 = input("Producto 1: ")
cant1 = int(input("Cantidad 1: "))

prod2 = input("Producto 2: ")
cant2 = int(input("Cantidad 2: "))

prod3 = input("Producto 3: ")
cant3 = int(input("Cantidad 3: "))

sub1 = prec1*cant1
sub2 = prec2*cant2
sub3 = prec3*cant3

subtotal = sub1 + sub2 + sub3

if subtotal >= 20000:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print(f"{cant1} x {prod1} \t {sub1}")
print(f"{cant2} x {prod2} \t {sub2}")
print(f"{cant3} x {prod3} \t {sub3}")
print(f"Subtotal \t {subtotal}")
print(f"Descuento \t {descuento}")
print(f"Total a pagar \t {total}")