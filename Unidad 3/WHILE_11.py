nota = input("Ingrese una nota del 1 al 10: ")
nota = int(nota)
while not (nota >= 1 and nota <= 10):
    nota = input("Error \nIngrese la nota nuevamente: ")
    nota = int(nota)
print("Bien hecho!")