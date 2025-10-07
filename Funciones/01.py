"""
Crear una función que solicite 15 números por el teclado,
y muestre por pantalla la suma de ellos
"""

def sumar_numeros():
    cont = 0
    suma = 0
    while cont < 15:
        cont += 1
        num = int(input(f"Numero {cont}: "))
        suma += num
    print(f"La suma es {suma}")

sumar_numeros()