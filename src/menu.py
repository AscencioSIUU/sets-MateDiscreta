import validator as val

#menu
def menu():
     print("Bienvenido a la calculadora de conjuntos")
     while True:
          print("1. Construir Conjuntos") 
          print("2. Operar conjuntos") 
          print("3. Finalizar") 
          choice = input("> Que desea hacer? :")
          if choice == '1':
               print("Construir Conjuntos")
          elif choice ==  '2':
               print("Operar conjuntos")
          elif choice == '3':
               print("Saliendo del programa...")
               break
          else:
               print("Opción no valida")
             
               




if __name__ == "__main__":
    menu()