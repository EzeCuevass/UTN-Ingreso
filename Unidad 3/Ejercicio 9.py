compra = input("Ingrese el valor de su compra: ")
compra = int(compra)

descuento = 25

compra_descontada = compra - compra * (descuento/100)

print(f"Su compra ha sido de ${compra}, con un descuento de un {descuento}% usted pagaria ${compra_descontada}")