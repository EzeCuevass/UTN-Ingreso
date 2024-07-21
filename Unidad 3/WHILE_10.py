contraseña = "anasheX"
i=0
while i < 3:
    intento = input("Ingrese su contraseña: ")
    if contraseña != intento:
        print("intente otra vez")
        i+=1
    else:
        print("Ingreso permitido!")
        break