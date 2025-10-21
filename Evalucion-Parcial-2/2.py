"""
Crea un programa que pida al usuario que ingrese números enteros de 
forma repetida. La entrada de datos debe detenerse solo cuando el usuario
ingrese el número 0. Al final, el programa debe mostrar el total de 
números pares y el total de números impares que se ingresaron.
"""

pares = 0
impares = 0

while True:
    numero = int(input("Numero: "))
    if numero == 0:
        break
    else:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"Totao de numeros pares: {pares}")
print(f"Total de numeros impares: {impares}")