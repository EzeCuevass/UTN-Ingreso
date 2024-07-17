sueldo = input("Ingrese su sueldo: ")
sueldo = int(sueldo)
estado_civil = input("Casado o Soltero?: ")
hijos = input("Cuantos hijos tiene?: ")
hijos = int(hijos)

if sueldo < 2200000 and estado_civil == "Casado" and hijos >=2:
    print("Usted no paga Impuesto a las ganancias")
else:
    print("Usted paga Impuesto a las ganancias")