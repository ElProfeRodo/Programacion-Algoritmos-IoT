"""
Solicitar el ingreso de un nombre que tenga por lo menos siete 
caracteres, en caso contrario, volver a pedirlo hasta que el 
valor del nombre cumpla con el requisito
"""

nombre = input("Nombre: ")

while len(nombre) < 7:
    print("Deben ser por lo menos 7 caracteres")
    nombre = input("Nombre: ")

while True:
    nombre = input("Nombre: ")
    if len(nombre) >= 7:
        break
    else:
        print("Deben ser por lo menos 7 caracteres")