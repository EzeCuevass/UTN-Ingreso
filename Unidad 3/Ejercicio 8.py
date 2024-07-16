sueldo = input("Ingrese su sueldo: ")
sueldo = int(sueldo)
porcentaje = input("Ingrese un porcentaje: ")
porcentaje = int(porcentaje)

aumento = sueldo * (porcentaje/100)
sueldo_aumentado = aumento + sueldo
print(f"Su sueldo actual es de {sueldo}, con un aumento de un {porcentaje}%, usted ganaria {sueldo_aumentado}")