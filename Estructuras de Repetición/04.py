"""
Solicitar números desde el teclado hasta que el usuario ingrese 
el valor cero. Luego, mostrar por pantalla la sumatoria de los números introducidos.
"""
# FORMA 1
sumatoria = 0
numero = int(input("Numero: "))

while numero != 0:
    sumatoria += numero
    # sumatoria = sumatoria + numero
    numero = int(input("Numero: "))

print(f"La suma es {sumatoria}")

# FORMA 2
sumatoria = 0
while True:
    numero = int(input("Numero: "))
    sumatoria += numero
    # sumatoria = sumatoria + numero
    if numero == 0:
        break
print(f"La suma es {sumatoria}")