def universo():
    abecedario_mayusculas = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numeros_0_9 = [str(i) for i in range(10)]
    return abecedario_mayusculas + numeros_0_9

def complemento(conjunto):
    universo_completo = universo()
    complemento_resultado = []
    
    # Calcular el complemento
    for elemento_universo in universo_completo:
        encontrado = False
        for elemento_conjunto in conjunto:
            if elemento_universo == elemento_conjunto:
                encontrado = True
                break
        if not encontrado:
            complemento_resultado.append(elemento_universo)
    
    return complemento_resultado

def union(ConjuntoA, ConjuntoB):
    # Inicializamos el conjunto final con los elementos de ConjuntoA
    union_resultado = ConjuntoA[:]
    
    # Recorremos cada elemento en ConjuntoB
    for elemento_B in ConjuntoB:
        encontrado = False
        # Verificamos si elemento_B ya está en ConjuntoA
        for elemento_A in ConjuntoA:
            if elemento_B == elemento_A:
                encontrado = True
                break
        # Si no está, lo agregamos al conjunto final
        if not encontrado:
            union_resultado.append(elemento_B)
    
    return union_resultado


def interseccion(ConjuntoA, ConjuntoB):
    interseccion_resultado = []
    
    # Recorremos cada elemento en ConjuntoA
    for elemento_A in ConjuntoA:
        # Verificamos si el elemento_A también está en ConjuntoB
        for elemento_B in ConjuntoB:
            if elemento_A == elemento_B:
                interseccion_resultado.append(elemento_A)
                break
    
    return interseccion_resultado
    
def diferencia(ConjuntoA, ConjuntoB):
    diferencia_resultado = []
    
    # Recorremos cada elemento en ConjuntoA
    for elemento_A in ConjuntoA:
        encontrado = False
        # Buscamos si elemento_A está en ConjuntoB
        for elemento_B in ConjuntoB:
            if elemento_A == elemento_B:
                encontrado = True
                break
        # Si no lo encontramos en ConjuntoB, lo agregamos al resultado
        if not encontrado:
            diferencia_resultado.append(elemento_A)
    
    return diferencia_resultado


def diferencia_simetrica(ConjuntoA, ConjuntoB):
    diferencia_A_B = []
    diferencia_B_A = []
    
    # Calcular A - B
    for elemento_A in ConjuntoA:
        encontrado = False
        for elemento_B in ConjuntoB:
            if elemento_A == elemento_B:
                encontrado = True
                break
        if not encontrado:
            diferencia_A_B.append(elemento_A)
    
    # Calcular B - A
    for elemento_B in ConjuntoB:
        encontrado = False
        for elemento_A in ConjuntoA:
            if elemento_B == elemento_A:
                encontrado = True
                break
        if not encontrado:
            diferencia_B_A.append(elemento_B)
    
    # Unimos ambas diferencias para obtener la diferencia simétrica
    diferencia_simetrica_resultado = diferencia_A_B + diferencia_B_A
    
    return diferencia_simetrica_resultado


conjunto1 = ["A", "B", "C","1","2","3"]
conjunto2 = ["A", "B", "C","4","5","6"]

print(union(conjunto1,conjunto2))
print(interseccion(conjunto1,conjunto2))
print(complemento(conjunto1))
print(diferencia(conjunto1,conjunto2))
print(diferencia_simetrica(conjunto1,conjunto2))

#https://www.disfrutalasmatematicas.com/conjuntos/calculadora-conjuntos.html
#https://calculadoradeconjuntos.site
