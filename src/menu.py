import validator as val
import operations as op
import os
import platform

def limpiar_consola():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("Bienvenido a la calculadora de conjuntos")
    conjuntoA = conjuntoB = conjuntoC = None
    
    while True:
        print("1. Construir Conjuntos") 
        print("2. Operar conjuntos") 
        print("3. Finalizar") 
        choice = input("> ¿Qué desea hacer? :")
        
        if choice == '1':
            print("Construir Conjuntos")
            conjuntoA, conjuntoB, conjuntoC = val.construirConjuntos()
            print(f"Conjunto A: {conjuntoA}")
            print(f"Conjunto B: {conjuntoB}")
            if conjuntoC:
                print(f"Conjunto C: {conjuntoC}")
            limpiar_consola()
                
        
        elif choice == '2':
            if conjuntoA is None and conjuntoB is None and conjuntoC is None:
                print("Ingresa primero los conjuntos.")
                
            else:
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")
                if conjuntoC:
                    print(f"Conjunto C: {conjuntoC}")
                operation = input("¿Qué operación desea realizar?: \n1. Universo\n2. Complemento\n3. Unión\n4. Intersección\n5. Diferencia\n6. Diferencia Simétrica\n> Operación a realizar: ")
                
                if operation == '1':
                    print(f"Conjunto Universo: {op.universo()}")
                    limpiar_consola()
                
                elif operation == '2':
                    print("Seleccione el conjunto para el complemento:")
                    if conjuntoA:
                        print("1. Conjunto A")
                    if conjuntoB:
                        print("2. Conjunto B")
                    if conjuntoC:
                        print("3. Conjunto C")
                    
                    conjunto_seleccionado = input("> Ingrese el número del conjunto: ")

                    if conjunto_seleccionado == '1' and conjuntoA:
                        print(f"Complemento de A: {op.complemento(conjuntoA)}")
                    elif conjunto_seleccionado == '2' and conjuntoB:
                        print(f"Complemento de B: {op.complemento(conjuntoB)}")
                    elif conjunto_seleccionado == '3' and conjuntoC:
                         print(f"Complemento de C: {op.complemento(conjuntoC)}")
                    else:
                        print("Selección no válida o conjunto no disponible.")

                elif operation == '3':
                    print("Seleccione los conjuntos para la unión:")
                    conjuntos = []
                    if conjuntoA:
                        print("1. Conjunto A")
                    if conjuntoB:
                        print("2. Conjunto B")
                    if conjuntoC:
                        print("3. Conjunto C")
                    
                    seleccion = input("> Ingrese los números de los conjuntos separados por comas (ejemplo: 1,2): ")
                    seleccion = seleccion.split(',')

                    for sel in seleccion:
                        if sel == '1' and conjuntoA:
                            conjuntos.append(conjuntoA)
                        elif sel == '2' and conjuntoB:
                            conjuntos.append(conjuntoB)
                        elif sel == '3' and conjuntoC:
                            conjuntos.append(conjuntoC)
                    
                    if conjuntos:
                        union = op.union(*conjuntos)
                        print(f"Unión de los conjuntos seleccionados: {union}")
                    else:
                        print("No se seleccionaron conjuntos válidos.")   

                elif operation == '4':
                    print("Seleccione los conjuntos para la intersección:")
                    conjuntos = []
                    if conjuntoA:
                        print("1. Conjunto A")
                    if conjuntoB:
                        print("2. Conjunto B")
                    if conjuntoC:
                        print("3. Conjunto C")
                    
                    seleccion = input("> Ingrese los números de los conjuntos separados por comas (ejemplo: 1,2): ")
                    seleccion = seleccion.split(',')

                    for sel in seleccion:
                        if sel == '1' and conjuntoA:
                            conjuntos.append(conjuntoA)
                        elif sel == '2' and conjuntoB:
                            conjuntos.append(conjuntoB)
                        elif sel == '3' and conjuntoC:
                            conjuntos.append(conjuntoC)
                    
                    if conjuntos:
                        interseccion = op.interseccion(*conjuntos)
                        print(f"Intersección de los conjuntos seleccionados: {interseccion}")
                    else:
                        print("No se seleccionaron conjuntos válidos.")

                elif operation == '5':
                    print("Seleccione los conjuntos para la diferencia:")
                    if conjuntoA and conjuntoB:
                        print("1. Diferencia A - B")
                        print("2. Diferencia B - A")
                        if conjuntoC:
                            print("3. Diferencia A - C")
                            print("4. Diferencia B - C")
                            print("5. Diferencia C - A")
                            print("6. Diferencia C - B")

                        seleccion = input("> Ingrese el número de la operación: ")

                        if seleccion == '1':
                            print(f"Diferencia A - B: {op.diferencia(conjuntoA, conjuntoB)}")
                        elif seleccion == '2':
                            print(f"Diferencia B - A: {op.diferencia(conjuntoB, conjuntoA)}")
                        elif seleccion == '3' and conjuntoC:
                            print(f"Diferencia A - C: {op.diferencia(conjuntoA, conjuntoC)}")
                        elif seleccion == '4' and conjuntoC:
                            print(f"Diferencia B - C: {op.diferencia(conjuntoB, conjuntoC)}")
                        elif seleccion == '5' and conjuntoC:
                            print(f"Diferencia C - A: {op.diferencia(conjuntoC, conjuntoA)}")
                        elif seleccion == '6' and conjuntoC:
                            print(f"Diferencia C - B: {op.diferencia(conjuntoC, conjuntoB)}")
                        else:
                            print("Selección no válida o conjuntos no disponibles.")
                    else:
                        print("Necesitas al menos los conjuntos A y B para esta operación.")

                elif operation == '6':
                    print("Seleccione los conjuntos para la diferencia simétrica:")
                    if conjuntoA and conjuntoB:
                        print("1. Diferencia Simétrica A - B")
                        if conjuntoC:
                            print("2. Diferencia Simétrica A - C")
                            print("3. Diferencia Simétrica B - C")

                        seleccion = input("> Ingrese el número de la operación: ")

                        if seleccion == '1':
                            print(f"Diferencia Simétrica A - B: {op.diferencia_simetrica(conjuntoA, conjuntoB)}")
                        elif seleccion == '2' and conjuntoC:
                            print(f"Diferencia Simétrica A - C: {op.diferencia_simetrica(conjuntoA, conjuntoC)}")
                        elif seleccion == '3' and conjuntoC:
                            print(f"Diferencia Simétrica B - C: {op.diferencia_simetrica(conjuntoB, conjuntoC)}")
                        else:
                            print("Selección no válida o conjuntos no disponibles.")
                    else:
                        print("Necesitas al menos los conjuntos A y B para esta operación.")
                    limpiar_consola()
                else:
                    print("Operación no válida.")


        elif choice == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
