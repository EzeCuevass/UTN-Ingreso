import math
lado_menor = 5  
lado_mayor = 6
diagonal_menor = 8

# varilla_diagonal_menor = ((lado_menor**2)-(diagonal_menor/2)**2)**0.5 
# varilla_diagonal_mayor = ((lado_mayor**2)-(diagonal_menor/2)**2)**0.5

varilla_diagonal_menor = math.sqrt(math.pow( lado_menor,2 ) - math.pow( diagonal_menor/2,2 ))
varilla_diagonal_mayor = math.sqrt(math.pow( lado_mayor,2 ) - math.pow( diagonal_menor/2,2 ))

diagonal_mayor = varilla_diagonal_mayor + varilla_diagonal_menor

perimetro = (lado_menor + lado_mayor) * 2

suma_varillas = perimetro + diagonal_menor + diagonal_mayor

area_cometa = (diagonal_menor * diagonal_mayor ) / 2

cola_cometa = area_cometa * 0.1

total_papel_un_cometa = area_cometa * cola_cometa 

total_varilla_mts = suma_varillas / 100

total_papel_mt = total_papel_un_cometa / 100

total_varillla_x10 = total_varilla_mts * 10
total_papel_x10 = total_papel_mt * 10 

print(total_papel_x10)
print(total_varillla_x10)