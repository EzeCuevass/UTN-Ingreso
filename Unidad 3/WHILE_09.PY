bandera = True
contraseña = "anasheX"
while bandera == True:
    intento = input("Ingrese su contraseña: ")
    if contraseña != intento:
        print("intente otra vez")
    else:
        print("Ingreso permitido!")
        break