color = input("Ingrese un color: ")

while not (color == "Rojo" or color == "Azul" or color == "Verde"):
    color = input("Error \nIngrese el color otra vez: ")
print("Bien hecho!")