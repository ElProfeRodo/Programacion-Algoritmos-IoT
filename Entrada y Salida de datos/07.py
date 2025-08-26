"""
Calcular la nota de presentación al examen, solicitando el ingreso de 4 calificaciones
y la ponderación de cada una de ellas. Las notas pueden ser números reales y las
ponderaciones deben ser números enteros. Mostrar el resultado por pantalla
"""

nota1 = float(input("Nota 1: "))
pond1 = int(input("Ponderación 1: "))
nota2 = float(input("Nota 2: "))
pond2 = int(input("Ponderación 2: "))
nota3 = float(input("Nota 3: "))
pond3 = int(input("Ponderación 3: "))
nota4 = float(input("Nota 4: "))
pond4 = int(input("Ponderación 4: "))

nota_final = nota1*(pond1/100) + nota2*(pond2/100) + nota3*(pond3/100) + nota4*(pond4/100)

print(f"Nota final es {nota_final:.0f}")
