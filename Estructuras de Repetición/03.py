"""
Solicitar la cantidad de número que el usuario desea introducir, 
luego solicitar esos números y devolver la sumatoria de los números impares.
"""

cantidad = int(input("Cantidad: "))
contador = 0
sumatoria = 0

while contador < cantidad:
    contador += 1
    numero = int(input("Numero: "))
    if numero % 2 != 0:
        sumatoria += numero
        # sumatoria = sumatoria + numero

print(f"La suma es {sumatoria}")