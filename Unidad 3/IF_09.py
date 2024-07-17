edad = input("Ingrese su edad: ")
edad = int(edad) 
nacionalidad = input("Naturalizado o Nativo?")
if (edad >= 16 and nacionalidad == "Nativo") or (edad >= 18 and nacionalidad=="Naturalizado"):
    print("Usted puede votar")
else:
    print("Usted NO puede votar")