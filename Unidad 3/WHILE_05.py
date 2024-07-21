i = 0

suma = 0

while i < 5:
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    suma += numero
    i+=1

promedio = suma / 5

print(promedio)