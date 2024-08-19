numberUniverse = set(map(str, range(0, 10)))
lettersUniverse = set(chr(c) for c in range(ord('A'), ord('Z') + 1))
validUniverse = numberUniverse.union(lettersUniverse)

def universeValidator(array):
    valid_elements = []
    for element in array:
        if len(element) == 1 and element.upper() in validUniverse:
            valid_elements.append(element.upper())
        else:
            print(f"Elemento no válido encontrado: {element}")
    return valid_elements

def ingresarConjunto(nombre_conjunto):
    conjunto = input(f"Ingrese el conjunto {nombre_conjunto} (separado por comas):").upper()  # Convertir todo a mayúsculas
    if not conjunto:
        print(f"El conjunto {nombre_conjunto} no puede estar vacío.")
        return None
    
    conjunto = list(map(str.strip, conjunto.split(',')))  # Dividir por comas y eliminar espacios en blanco
    conjunto_validado = universeValidator(conjunto)
    
    return conjunto_validado

def construirConjuntos():
    conjuntoA = ingresarConjunto("A")
    conjuntoB = ingresarConjunto("B")

    opcion = input("¿Desea ingresar otro conjunto (C)? (s/n): ").strip().lower()
    if opcion == 's':
        conjuntoC = ingresarConjunto("C")
    else:
        conjuntoC = None

    return conjuntoA, conjuntoB, conjuntoC
