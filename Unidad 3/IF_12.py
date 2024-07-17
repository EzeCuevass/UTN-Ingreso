import random
nota = random.randint(1,10)

if nota >= 6:
    print(f"Promoción directa, la nota es {nota}")
elif nota < 6 and nota > 3:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")