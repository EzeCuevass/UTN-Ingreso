i = 0

min = 0

max = 0
while i < 10:
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    i+=1
    if numero > max:
        max = numero
        min = numero
    if numero < min:
        min = numero
print(min)
print(max)