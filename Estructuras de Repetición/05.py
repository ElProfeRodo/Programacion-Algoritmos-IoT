"""
Solicitar números desde el teclado hasta que el usuario ingrese 
el valor cero. Luego, mostrar por pantalla el promedio de los números 
positivos
"""

numero = int(input("Numero: ")) #5
cont = 0
suma = 0

while numero != 0:
    if numero > 0:
        suma += numero
        cont += 1
    numero = int(input("Numero: "))

promedio = suma / cont
print(f"El promedio es {promedio}")