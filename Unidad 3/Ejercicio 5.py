numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese otro numero: ")
numero1 = int(numero1)
numero2 = int(numero2) 
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

mensaje = f"La suma de los numeros es igual a {suma}\n" 
mensaje += f"La resta de los numeros es igual a {resta}\n"
mensaje += f"La multiplicacion de los numeros es igual a {multiplicacion}\n"
mensaje += f"La division de los numeros es igual a {division}\n"

print(mensaje)