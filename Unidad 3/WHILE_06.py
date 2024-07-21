suma = 0

bandera = True

while bandera == True:
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    suma += numero
    opcion = input("Si para ingresar otro numero")
    if opcion != "Si":
        break

print(suma)