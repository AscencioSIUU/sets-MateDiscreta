import validator as val

def menu():
     print("Bienvenido a la calculadora de conjuntos")
     while True:
          print("1. Construir Conjuntos") 
          print("2. Operar conjuntos") 
          print("3. Finalizar") 
          choice = input("> Que desea hacer? :")
          if choice == '1':
               print("Construir Conjuntos")
               conjuntoA, conjuntoB, conjuntoC = val.construirConjuntos()
               print(f"Conjunto A: {conjuntoA}")
               print(f"Conjunto B: {conjuntoB}")
               if conjuntoC:
                    print(f"Conjunto C: {conjuntoC}")
          elif choice ==  '2':
               print("Operar conjuntos")
               # Aquí puedes agregar el código para operar con los conjuntos
          elif choice == '3':
               print("Saliendo del programa...")
               break
          else:
               print("Opción no valida")

if __name__ == "__main__":
    menu()
