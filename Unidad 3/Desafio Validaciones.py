apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
edad = int(edad)
estado_civil = input("Ud es Soltero, Casado, Divorciado o Viudo?")
numero_legajo = input("Ingrese su numero de legajo: ")

while True: 
    if edad < 18 or edad > 90:
        edad = input("Error, ingrese nuevamente su edad")
        edad = int(edad)
    if estado_civil != "Soltero" or estado_civil != "Casado" or estado_civil != "Divorciado" or estado_civil != "Viudo":
        estado_civil = input("Error, ingrese nuevamente su estado civil")
        