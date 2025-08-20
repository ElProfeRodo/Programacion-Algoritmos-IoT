"""
Calcular la edad de un usuario. El usuario debe ingresar su nombre y año de
nacimiento. Por pantalla se debe mostrar:
Hola [USUARIO], tienes [EDAD] años.
"""

nombre = input("Ingresa nombre: ")
anio_nacto = int(input("Ingresa año nacimiento: "))

edad = 2025 - anio_nacto

print(f"Hola {nombre}, tienes {edad} años")
