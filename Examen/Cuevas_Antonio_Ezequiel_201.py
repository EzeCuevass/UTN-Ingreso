# Condicion para continuar
continuar  = "si"
# Acumuladores
acumulador_fem_mp = 0
# Inicializacion de minimo y bandera para el primer voto de bautista
primer_voto_bautista = True
min_primer_voto_bautista = 0
# Contadores
contador_fem_mp = 0
contador_furia = 0
contador_emma = 0
contador_bautista = 0
contador_masc_25_40 = 0

while continuar == "si":
    # Ingreso de datos
    nombre = input("Introduzca su nombre: ")
    
    edad = input("Introduzca su edad: ")
    edad = int(edad)
    while edad <= 13:
        edad = input("Error. Introduzca su edad nuevamente: ")
        edad = int(edad)

    genero = input("Introduzca su genero: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Error, ingrese nuevamente su genero: ")
    
    voto = input("A quien esta destinado su voto?: ")
    while voto != "Emma" and voto != "Furia" and voto != "Bautista":
        voto = input("Error, ingrese nuevamente su voto: ")
    
    mp = input("Realiza el pago por Mercado Pago?: ")
    if mp == "si" or mp == "Si" or mp == "SI":
        mp = True
    else:
        mp = False
    continuar = input("Desea ingresar otro voto?: ")
    # Lógica 
    
    # 1. El promedio de edad de las votantes de género femenino que realizaron el pago con
    # mercado pago..
    if genero == "Femenino": 
        if mp == True:
            contador_fem_mp += 1
            acumulador_fem_mp += edad
    else:
        # 5. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a
        # Emma.
        if (edad >= 25 and edad <= 40) and (voto == "Furia" or voto == "Emma"):
            contador_masc_25_40 += 1
    
    # 2. El nombre del participante que ganó el reality (El que tiene más votos).
    if voto == "Furia":
        contador_furia += 1
    elif voto == "Emma":
        contador_emma += 1
    else:
        # 3. Nombre del votante más joven qué votó a Bautista.
        if primer_voto_bautista == True:
            min_primer_voto_bautista = edad
            contador_bautista += 1
            primer_voto_bautista = False
        if edad < min_primer_voto_bautista:
            min_primer_voto_bautista = edad
            contador_bautista += 1
    

# Salida de datos

# 1. El promedio de edad de las votantes de género femenino que realizaron el pago con mercado pago..
if contador_fem_mp > 0:
    promedio_fem_mp = acumulador_fem_mp / contador_fem_mp
    print(f"El promedio de edad de las votantes que pagaron con Mercado Pago es de: {promedio_fem_mp}")
else:
    print("No se puede obtener un promedio de edad de las votantes femeninas que pagaron con Mercado Pago")

# 2. El nombre del participante que ganó el reality (El que tiene más votos).
if contador_furia > contador_emma and contador_furia > contador_bautista:
    print("La ganadora es Furia")
elif contador_emma > contador_furia and contador_emma > contador_bautista:
    print("La ganadora es Emma")
elif contador_bautista > contador_furia and contador_bautista > contador_emma:
    print("El ganador es Bautista")
else:
    print("Hubo un empate al definir el ganador del certamen")

# 3. Nombre del votante más joven qué votó a Bautista.
if min_primer_voto_bautista > 0:
    print(f"El votante mas joven de Bautista tiene {min_primer_voto_bautista}")
else:
    print("No se obtuvieron votos a Bautista")

# 4. Nombre de cada participante y porcentaje de los votos que recibió.
total_votos = contador_bautista + contador_emma + contador_furia
print(f"Furia obtuvo un {contador_furia*100/total_votos}% de votos")
print(f"Emma obtuvo un {contador_emma*100/total_votos}% de votos")
print(f"Bautista obtuvo un {contador_bautista*100/total_votos}% de votos")

# 5. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Furia o a Emma.
if contador_masc_25_40 > 0:
    mensaje = f"La cantidad de personas de genero masculino entre 25 y 40 años en votar a Furia o Emma es de "
    mensaje += f"{contador_masc_25_40}"
    print(mensaje)
else:
    print("No hubo personas de genero masculino entre 25 y 40 años en votar a Furia o Emma")