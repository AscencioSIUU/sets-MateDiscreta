# Definir el universo de números y letras
numberUniverse = set(map(str, range(0, 10)))
lettersUniverse = set(chr(c) for c in range(ord('A'), ord('Z') + 1))
validUniverse = numberUniverse.union(lettersUniverse)

#Valida los elementos de un array, asegurando que sean parte del universo válido (números o letras).
def universeValidator(array):
    valid_elements = []
    for element in array:
        # Verifica si el elemento es válido
        if len(element) == 1 and element.upper() in validUniverse:
            # Agrega el elemento válido en mayúsculas
            valid_elements.append(element.upper())
        else:
            # Mensaje de error
            print(f"Elemento no válido encontrado: {element}")
    return valid_elements


# Solicita al usuario que ingrese un conjunto de elementos, los valida y los convierte a mayúsculas.
def ingresarConjunto(nombre_conjunto):
    conjunto = input(f"Ingrese el conjunto {nombre_conjunto} (separado por comas):").upper()  # Convertir todo a mayúsculas
     # Verifica que el conjunto no esté vacío
    if not conjunto:
        print(f"El conjunto {nombre_conjunto} no puede estar vacío.")
        return None
    
    conjunto = list(map(str.strip, conjunto.split(',')))  # Dividir por comas y eliminar espacios en blanco
    conjunto_validado = universeValidator(conjunto)
    
    return conjunto_validado

def construirConjuntos():
    # Pide ingresar dos o tres conjuntos, los valida y los retorna
    conjuntoA = ingresarConjunto("A")
    conjuntoB = ingresarConjunto("B")

    opcion = input("¿Desea ingresar otro conjunto (C)? (s/n): ").strip().lower()
    if opcion == 's':
        conjuntoC = ingresarConjunto("C")
    else:
        conjuntoC = None

    # Retorno de conjuntos
    return conjuntoA, conjuntoB, conjuntoC
