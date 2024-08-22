def universo():
    abecedario_mayusculas = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numeros_0_9 = [str(i) for i in range(10)]
    return abecedario_mayusculas + numeros_0_9

def complemento(conjunto):
    # Obtenemos el universo completo
    universo_completo = universo()
    
    # Calculamos el complemento restando los elementos del conjunto dado al universo
    complemento_resultado = [elemento for elemento in universo_completo if elemento not in conjunto]
    
    return complemento_resultado

def union(ConjuntoA, ConjuntoB):
    Final = list(ConjuntoA)

    # Iteramos sobre el segundo conjunto
    for elemento in ConjuntoB:
        # Solo agregamos los elementos que no estén ya en el conjunto final
        if elemento not in Final:
            Final.append(elemento)
    
    return Final


def interseccion(ConjuntoA, ConjuntoB):
    return [elemento for elemento in ConjuntoA if elemento in ConjuntoB]
    
    
def diferencia(ConjuntoA, ConjuntoB):
    # Calculamos la diferencia incluyendo solo los elementos de ConjuntoA que no están en ConjuntoB
    diferencia_resultado = [elemento for elemento in ConjuntoA if elemento not in ConjuntoB]
    
    return diferencia_resultado


def diferencia_simetrica(ConjuntoA, ConjuntoB):
    # Calculamos A - B
    diferencia_A_B = diferencia(ConjuntoA, ConjuntoB)
    
    # Calculamos B - A
    diferencia_B_A = diferencia(ConjuntoB, ConjuntoA)
    
    # La diferencia simétrica es la unión de A - B y B - A
    diferencia_simetrica_resultado = diferencia_A_B + diferencia_B_A
    
    return diferencia_simetrica_resultado

# conjunto1 = ["A", "B", "C","1","2","3"]
# conjunto2 = ["A", "B", "C","4","5","6"]

# print(union(conjunto1,conjunto2))
# print(interseccion(conjunto1,conjunto2))
# print(complemento(conjunto1))
# print(diferencia(conjunto1,conjunto2))
# print(diferencia_simetrica(conjunto1,conjunto2))

#https://www.disfrutalasmatematicas.com/conjuntos/calculadora-conjuntos.html
#https://calculadoradeconjuntos.site
