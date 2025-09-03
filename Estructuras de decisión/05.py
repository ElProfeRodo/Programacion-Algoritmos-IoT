"""
Pedir el ingreso de un teléfono y verificar que la cantidad de números sea igual que
nueve. Mostrar el resultado por pantalla.
"""
telefono = input("Telefono: ")

if len(telefono) == 9:
    print("Telefono valido")
else:
    print("Debe tener 9 digitos")