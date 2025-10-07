"""
Crear una función que reciba como parámetro un nombre 
y un apellido, genere la dirección de correo electrónico 
Gmail con esos datos y muestre por pantalla el resultado.
rodolfo.fernandez@gmail.com
"""

def generar_correo(nombre, apellido):
    correo = f"{nombre}.{apellido}@gmail.com"
    print(correo)

nombre = input("Nombre: ")
apellido = input("Apellido: ")
generar_correo(nombre, apellido)