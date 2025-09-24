"""
Solicitar un número desde el teclado y validar que sea positivo. 
En caso de no serlo, volver a pedir el número hasta que supere la validación
"""

# FORMA 1
numero = int(input("Numero: "))

while numero <= 0:
    numero = int(input("Numero: "))

# FORMA 2
while True:
    numero = int(input("Numero: "))
    if numero > 0:
        break