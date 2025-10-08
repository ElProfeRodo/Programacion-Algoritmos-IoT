def sumar_impares(minimo, maximo):
    suma = 0
    while minimo <= maximo:
        # Si es impar
        if minimo % 2 != 0:
            suma += minimo
        minimo += 1
    return suma

sumatoria = sumar_impares(1, 4)
print(f"La suma de los impares es {sumatoria}")