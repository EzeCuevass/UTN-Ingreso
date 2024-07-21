suma = 0
multiplicacion = 1
bandera = True

while bandera == True:
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    suma += numero
    if numero < 0:
        multiplicacion *= numero
    opcion = input("Si para ingresar otro numero: ")
    if opcion != "Si":
        break

print(suma)
print(multiplicacion)