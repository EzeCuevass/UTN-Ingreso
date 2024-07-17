altura = input("Ingrese su altura en metros: ")
altura = float(altura)

if (altura < 1.60):
    print("Su posicion en cancha es base")
elif (altura >= 1.60 and altura <= 1.79):
    print("Su posicion en cancha es escolta")
elif (altura >= 1.80 and altura <= 1.99):
    print("Su posicion en cancha es alero")
else:
    print("Su posicion en cancha es ala-pivot o pivot")