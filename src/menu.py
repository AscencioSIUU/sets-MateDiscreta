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
        choice = input("> ¿Qué desea hacer? : ")
        
        if choice == '1':
            print("Construir Conjuntos")
            conjuntoA, conjuntoB, conjuntoC = val.construirConjuntos()
            print(f"Conjunto A: {conjuntoA}")
            print(f"Conjunto B: {conjuntoB}")
            if conjuntoC:
                print(f"Conjunto C: {conjuntoC}")
            limpiar_consola()
                
        
        elif choice == '2':
            # Valida que se hayan ingresado los conjuntos
            if conjuntoA is None or conjuntoB is None or conjuntoC is None:
                print("Ingresa primero los conjuntos A y B.")
                
            if len(conjuntoA) == 0 or len(conjuntoB) == 0 or len(conjuntoC) == 0:
                print("Ocurrio un error, uno de los conjuntos es vacio.")
                print("Ingrese correctamente lo conjuntos.")
                 
           # Realiza las diferentes opreaciones
            else:
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")
                if conjuntoC:
                    print(f"Conjunto C: {conjuntoC}")
                operation = input("¿Qué operación desea realizar?: \n1. Universo\n2. Complemento\n3. Unión\n4. Intersección\n5. Diferencia\n6. Diferencia Simétrica\n> Operación a realizar: ")
                # Realiza operacion de Universo
                if operation == '1':
                    print(f"Conjunto Universo: {op.universo()}")
                    
                # Realiza operacion de complemento
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
 
                # Realiza operacion de unión
                elif operation == '3':
                    print("Seleccione los conjuntos para la unión:")
                    if conjuntoA and conjuntoB:
                        print("1. Unión A ∪ B")
                    if conjuntoA and conjuntoC:
                        print("2. Unión A ∪ C")
                    if conjuntoB and conjuntoC:
                        print("3. Unión B ∪ C")
                    
                    seleccion = input("> Ingrese el número de la operación: ")

                    if seleccion == '1':
                        print(f"Unión A ∪ B: {op.union(conjuntoA, conjuntoB)}")
                    elif seleccion == '2' and conjuntoC:
                        print(f"Unión A ∪ C: {op.union(conjuntoA, conjuntoC)}")
                    elif seleccion == '3' and conjuntoC:
                        print(f"Unión B ∪ C: {op.union(conjuntoB, conjuntoC)}")
                    else:
                        print("Selección no válida o conjuntos no disponibles.")
  
                # Realiza operacion de intersección
                elif operation == '4':
                    print("Seleccione los conjuntos para la intersección:")
                    if conjuntoA and conjuntoB:
                        print("1. Intersección A ∩ B")
                    if conjuntoA and conjuntoC:
                        print("2. Intersección A ∩ C")
                    if conjuntoB and conjuntoC:
                        print("3. Intersección B ∩ C")
                    
                    seleccion = input("> Ingrese el número de la operación: ")

                    if seleccion == '1':
                        print(f"Intersección A ∩ B: {op.interseccion(conjuntoA, conjuntoB)}")
                    elif seleccion == '2' and conjuntoC:
                        print(f"Intersección A ∩ C: {op.interseccion(conjuntoA, conjuntoC)}")
                    elif seleccion == '3' and conjuntoC:
                        print(f"Intersección B ∩ C: {op.interseccion(conjuntoB, conjuntoC)}")
                    else:
                        print("Selección no válida o conjuntos no disponibles.")

                # Realiza operacion de diferencia
                elif operation == '5':
                    print("Seleccione los conjuntos para la diferencia:")
                    if conjuntoA and conjuntoB:
                        print("1. Diferencia A - B")
                        print("2. Diferencia B - A")
                    if conjuntoA and conjuntoC:
                        print("3. Diferencia A - C")
                    if conjuntoB and conjuntoC:
                        print("4. Diferencia B - C")
                    if conjuntoC and conjuntoA:
                        print("5. Diferencia C - A")
                    if conjuntoC and conjuntoB:
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

                # Realiza operacion de diferencia simétrica
                elif operation == '6':
                    print("Seleccione los conjuntos para la diferencia simétrica:")
                    if conjuntoA and conjuntoB:
                        print("1. Diferencia Simétrica A Δ B")
                    if conjuntoA and conjuntoC:
                        print("2. Diferencia Simétrica A Δ C")
                    if conjuntoB and conjuntoC:
                        print("3. Diferencia Simétrica B Δ C")

                    seleccion = input("> Ingrese el número de la operación: ")

                    if seleccion == '1':
                        print(f"Diferencia Simétrica A Δ B: {op.diferencia_simetrica(conjuntoA, conjuntoB)}")
                    elif seleccion == '2' and conjuntoC:
                        print(f"Diferencia Simétrica A Δ C: {op.diferencia_simetrica(conjuntoA, conjuntoC)}")
                    elif seleccion == '3' and conjuntoC:
                        print(f"Diferencia Simétrica B Δ C: {op.diferencia_simetrica(conjuntoB, conjuntoC)}")
                    else:
                        print("Selección no válida o conjuntos no disponibles.")


                else:
                    print("Operación no válida.")
                    limpiar_consola()
     
        elif choice == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida")
            limpiar_consola()

if __name__ == "__main__":
    menu()
