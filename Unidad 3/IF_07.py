edad = input("Ingrese su edad: ")
edad = int(edad)

if (edad <=10):
    print("Usted es un niño")
elif (edad > 10 and edad <13):
    print("Usted es pre-adolescente")
elif (edad >= 13 and edad <=17):
    print("Usted es adolescente")
else: 
    print("Usted es mayor de edad")