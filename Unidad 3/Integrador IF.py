marca = input("Que marca va a comprar?: ")
cantidad = input("Cuantas lamparas va a comprar?: ")
cantidad = int(cantidad)
precio = 800 * cantidad

message = f"La marca de las lamparas es: {marca}\n"
message += f"La cantidad comprada es {cantidad}\n"
message += f"El precio sin descuento es de ${precio}\n"

descuento_adicional = 0
porcentaje = 0

if cantidad >= 6:
    porcentaje = 50
elif cantidad == 5:
    if marca == "ArgentinaLuz":
        porcentaje = 40
    else:
        porcentaje = 30
elif cantidad == 4:
    if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
        porcentaje = 25
    else:
        porcentaje = 20
elif cantidad == 3:
    if marca == "ArgentinaLuz":
        porcentaje = 15
    elif marca == "FelipeLamparas":
        porcentaje = 10
    else:
        porcentaje = 5

total = precio
precio_descuento = precio * porcentaje/100

if precio_descuento >= 4000:
    descuento_adicional = total * 5/100

if precio_descuento > 0:
    total = total - precio_descuento
    message += f"El descuento conseguido es de ${precio_descuento}\n"

if descuento_adicional > 0:
    total = total - descuento_adicional
    message += f"El descuento adicional es de ${descuento_adicional}\n" 

message += f"El total es de ${total}\n"
print(message)