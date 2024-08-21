def universo():
    abecedario_mayusculas = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numeros_0_9 = [str(i) for i in range(10)]
    print(abecedario_mayusculas)
    print(numeros_0_9)



def union(ConjuntoA, ConjuntoB):
    Final = list(ConjuntoA)

    # Iteramos sobre el segundo conjunto
    for elemento in ConjuntoB:
        # Solo agregamos los elementos que no estén ya en el conjunto final
        if elemento not in Final:
            Final.append(elemento)
    
    return Final



    
    


conjunto1 = ["a", "b", "c","1","2","3"]
conjunto2 = ["a", "b", "c","4","5","6"]

print(union(conjunto1,conjunto2))

