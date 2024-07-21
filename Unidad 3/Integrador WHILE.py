i = 0
numeros_negativos = 0
numeros_positivos = 0
max = 0
suma_negativos = 0
suma_positivos = 0
numero = 0
while (numero > -10000 and numero < 10000):
    i += 1
    numero = input("Ingresa un numero: ")
    numero = int(numero)
    if numero < 0:
        suma_negativos+= numero
        numeros_negativos += 1
    else:
        suma_positivos+= numero
        numeros_positivos += 1
    if numero > max:
        max = numero
    opcion = input("Enter para ingresar otro numero: ")
    if opcion != "":
        break
message = f"La suma acumulada de los numeros negativos es: {suma_negativos}"
message += f"\nLa suma acumulada de los numeros positivos es: {suma_positivos}"
message += f"\nLa cantidad de numeros negativos ingresados es: {numeros_negativos}"
message += f"\nEl promedio de numeros positivos es {suma_positivos/numeros_positivos}"
message += f"\nEl numero positivo mas grande es: {max}"
message += f"\nEl porcentaje de numeros negativos ingresados respecto al total es de un %{numeros_negativos*100/i}"
print(message)