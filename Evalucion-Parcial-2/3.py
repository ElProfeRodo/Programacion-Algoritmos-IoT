"""
Escribe un programa que presente un menú al usuario para que elija una 
conversión de temperatura:
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Salir
El programa debe usar un bucle while para seguir mostrando el menú y 
permitiendo conversiones hasta que el usuario elija la opción "3".
Para cada opción de conversión, crea una función separada 
(celsius_a_fahrenheit() y fahrenheit_a_celsius()) que reciba 
la temperatura, realice el cálculo y retorne el resultado.
Utiliza una estructura if para controlar la opción seleccionada 
por el usuario.
Fórmulas:
Fahrenheit=(Celsius*9/5)+32
Celsius=(Fahrenheit-32)*5/9
"""

def celsius_a_fahrenheit(temp):
    temp_f = (temp*9/5)+32
    return temp_f

def fahrenheit_a_celsius(temp):
    temp_c = (temp-32)*5/9
    return temp_c

while True:
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        temp_celsius = float(input("Temp C: "))
        temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
        print(f"Temp F: {temp_fahrenheit}")

    elif opcion == 2:
        temp_fahrenheit = float(input("Temp F: "))
        temp_celsius = fahrenheit_a_celsius(temp_fahrenheit)
        print(f"Temp C: {temp_celsius}")

    elif opcion == 3:
        break

    else:
        print("La opcion es incorrecta")