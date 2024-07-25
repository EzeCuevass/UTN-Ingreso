
condicion = "si"
velocidad_platillo = 0
velocidad_esfera = 0
velocidad_ovalada = 0
contador_platillo = 0
contador_esfera = 0
contador_ovalada = 0
contador_velocidad_mensaje = 0
avistamientos = 0
contador_claro = 0
contador_incomprensible = 0
contador_mercedes = 0
contador_250_esferica = 0
maximo_incomprensibles_esferica = 0
maximo_incomprensibles_ovalada = 0
maximo_incomprensibles_platillo = 0
nombre_empleado = ""

while condicion == "si": 
    avistamientos += 1
    nombre = input("Ingrese el nombre: ")
    #F. Si por lo menos algún empleado se llama “Mercedes” 
    if nombre == "Mercedes":
        contador_mercedes += 1
    forma = input("Como es la forma de la nave?: ")
    while forma != "Platillo" and forma != "Esferica" and forma != "Ovalada":
        forma = input("Error, ingrese otra vez la forma de la nave: ")
    velocidad = input("Cual es la velocidad maxima de la nave? (Mayor a 100 km/h): ")
    velocidad = int(velocidad)
    while velocidad < 100:
        velocidad = input("Error, ingrese otra vez la velocidad de la nave: ")
        velocidad = int(velocidad)
    tipo_mensaje = input("El mensaje fue? (Ninguno/Claro/Incomprensible): ")
    while tipo_mensaje != "Ninguno" and tipo_mensaje != "Claro" and tipo_mensaje != "Incomprensible":
        tipo_mensaje = input("Error, ingrese el tipo de mensaje otra vez: ")
    condicion = input("Ingrese si para informar otro avistamiento: ")
    #A. Velocidad promedio según la forma de la nave.
    if forma == "Platillo":
        contador_platillo += 1
        velocidad_platillo += velocidad
    elif forma == "Esferica":
        contador_esfera += 1
        velocidad_esfera += velocidad
    else:
        contador_ovalada += 1
        velocidad_ovalada += velocidad
    #B. Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la velocidad se encuentre 
    # entre los 200 km/h y los 500 km/h.
    #E. Cantidad de avistamientos que superen los 250 Km/h, cuyo mensaje sea Claro o incomprensible y que sea 
    # de tipo Esférica.
    #D. Nombre del empleado y forma de la nave del avistamiento con mensajes Incomprensibles, de las naves que resultaron 
    # ser más rápidas.
    if tipo_mensaje != "Ninguno":
        if (velocidad >= 200 and velocidad <= 500):
            contador_velocidad_mensaje += 1
            if velocidad > 250 and contador_esfera:
                contador_250_esferica += 1
            if tipo_mensaje == "Claro":
                contador_claro += 1
            elif tipo_mensaje == "Incomprensible":
                contador_incomprensible += 1
        elif tipo_mensaje == "Claro":
            contador_claro += 1
        elif tipo_mensaje == "Incomprensible":
            if contador_incomprensible == 0:
                if forma == "Esferica":
                    maximo_incomprensibles_esferica = velocidad
                elif forma == "Ovalada":
                    maximo_incomprensibles_ovalada = velocidad
                else:
                    maximo_incomprensibles_platillo = velocidad
            if maximo_incomprensibles_platillo < velocidad:
                maximo_incomprensibles_platillo = velocidad
            if maximo_incomprensibles_ovalada < velocidad:
                maximo_incomprensibles_ovalada = velocidad
            if maximo_incomprensibles_esferica < velocidad:
                maximo_incomprensibles_esferica = velocidad
            contador_incomprensible += 1

    if condicion != "si":
        break
if contador_esfera > 0:
    promedio_esferica = velocidad_esfera / contador_esfera
    mensaje = f"Velocidad promedio Esferica: {promedio_esferica}\n"
else:
    mensaje = "No se tienen avistamientos para realizar el promedio de la velocidad de las naves esfericas\n"
if contador_ovalada > 0:
    promedio_ovalada = velocidad_ovalada / contador_ovalada
    mensaje += f"Velocidad promedio ovalada: {promedio_ovalada}\n"
else:
    mensaje += "No se tienen avistamientos para realizar el promedio de la velocidad de las naves ovaladas\n"
if contador_platillo > 0:
    promedio_platillo = velocidad_platillo / contador_platillo
    mensaje += f"Velocidad promedio platillo: {promedio_platillo}\n"
else:
    mensaje += "No se tienen avistamientos para realizar el promedio de la velocidad de las naves platillo\n"
porcentaje_avistamiento_mensaje =  contador_velocidad_mensaje * 100 / avistamientos
#A. Velocidad promedio según la forma de la nave.
print(mensaje)
#B. Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la velocidad se encuentre 
# entre los 200 km/h y los 500 km/h.
print(f"El porcentaje de avistamientos con algun tipo de mensaje es de: %{porcentaje_avistamiento_mensaje}")
#C. Tipo de mensaje menos recibido.
if contador_incomprensible < contador_claro:
    print("El tipo de mensaje menos recibido fue: Incomprensible")
elif contador_claro < contador_incomprensible:
    print("El tipo de mensaje menos recibido fue: Claro")
else:
    print("Los mensajes Claro e Incomprensibles fueron recibidos de igual manera")
#E. Cantidad de avistamientos que superen los 250 Km/h, cuyo mensaje sea Claro o incomprensible y que sea 
# de tipo Esférica.
print(f"La cantidad de avistamientos con un tipo de mensaje de naves esfericas superando 250 km/h es de: {contador_250_esferica}")
#F. Si por lo menos algún empleado se llama “Mercedes” 
if contador_mercedes > 0:
    print("Una empleada que hizo un avistamiento se llama Mercedes")
else:
    print("Ninguna empleada con avistamientos se llama Mercedes")