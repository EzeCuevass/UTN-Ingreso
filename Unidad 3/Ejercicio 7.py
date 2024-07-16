sueldo = input("Ingrese su sueldo: ")
sueldo = float(sueldo)
porcentaje = 15

aumento = sueldo * (porcentaje/100)
sueldo_aumentado = sueldo + aumento

print(f"Con un aumento del {porcentaje}%, se le suman ${aumento} a su sueldo, por lo que ganaria ${sueldo_aumentado}")