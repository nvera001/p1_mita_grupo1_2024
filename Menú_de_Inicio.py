from Operaciones_CRUD import leer,crear,actualizar,eliminar
print()
#Se define la lista de los productos.
productos = [
    [1001,"Jugo de Manzana",50000],
    [1002,"Jugo de Pomelo",4000],
    [1003,"Coca",6000],
    [1004,"Coca",80000],
    [1005,"Agua",5000],
    [1005,"Fanta",6000],
    [1006,"Chocolate",4000],
    [1007,"Rocklets",1000],
    [1008,"Chupetín",500],
    [1009,"Caramelos",100],
        ]

def menu_de_inicio():
    print("Bienvenido a la aplicación del supermercado.")
    flag = True
    while flag!=False:
        inicio=input("\nQué desea realizar? \n1 Muestra de registros.\n2 Agregar nuevos registros a la lista.\n3 Editar un registro de la lista. \n4 Eliminar un registro de la lista. \n5 Salir de la aplicación. \nElija un numero: ") #Menú de inicio.
        if int (inicio)==1: #Muestra de registros.
            leer (productos)
            flag = False
            muest = input("\nQué desea realizar ahora? \n1 Volver al menú. \n2 Salir de la aplicación \nPor favor, elegir un número. ")
            if int(muest) == 1:
                flag = True
            if int(muest) == 2:
                print()
                print("Saliendo de la aplicación")
                flag = False
       
       
        
        elif int (inicio) == 2: #Agregar nuevos registros.
            print()
            crear(productos)
            flag = False
            print()
            inicio_2=input("Finalizada la creación de su registro, que desea realizar ahora?\n1 Ver el listado de los productos.\n2 Volver al menú de inicio.\n3 Salir de la aplicación. \nElegir una opción: ")
            
            if  int (inicio_2) == 1: #Ver el listado de los registros, incluido el nuevo.
                leer(productos)
                muest = input("\nQué desea realizar ahora? \n1 Volver al menú. \n2 Salir de la aplicación \nPor favor, elegir un número. ")
                if int(muest) == 1: #Volver al menú, despues de ver el listado de los registros (incluyendo al nuevo)
                    flag = True
                if int(muest) == 2:
                    print()
                    print("Saliendo de la aplicación") #Salir de la aplicacion,, despues de ver el listado de los registros (incluyendo al nuevo)
                    flag = False
                                        
            elif  int (inicio_2)==2: #Volver al menu principal, sin ver el listado nuevo.
                menu_de_inicio()
                flag = False
            elif int(inicio_2)==3: #Salir de la aplicacion, sin ver el listado nuevo.
                print()
                print("Saliendo de la aplicación.")
                flag = False



        elif int (inicio) == 3: #Editar un registro de la lista.
            print()
            actualizar (productos)
            print()
            inicio_2=input("Finalizada la actualización, que desea realizar ahora?\n1 Ver el listado de los productos.\n2 Volver al menú de inicio.\n3 Salir de la aplicación. \nElegir una opción: ")
            
            if  int (inicio_2) == 1: #Ver el listado de los registros, incluido el nuevo.
                leer(productos)
                muest = input("\nQué desea realizar ahora? \n1 Volver al menú. \n2 Salir de la aplicación \nPor favor, elegir un número. ")
                if int(muest) == 1: #Volver al menú, despues de ver el listado de los registros (incluyendo al nuevo)
                    print("Volviendo al menú principal.")
                    print()
                elif int(muest) == 2:
                    print()
                    print("Saliendo de la aplicación") #Salir de la aplicacion,, despues de ver el listado de los registros (incluyendo al nuevo)
                    flag = False
                                        
            elif  int (inicio_2)==2: #Volver al menu principal, sin ver el listado nuevo.
                menu_de_inicio()
                flag = False
            elif int(inicio_2)==3: #Salir de la aplicacion, sin ver el listado nuevo.
                print()
                print("Saliendo de la aplicación.")
                flag = False


        elif int (inicio) == 4: #Eliminar uno de los registros.
            eliminar(productos)
            print()
            inicio_2=input("Finalizada la eliminación, que desea realizar ahora?\n1 Ver el listado de los productos.\n2 Volver al menú de inicio.\n3 Salir de la aplicación. \nElegir una opción: ")
            
            if  int (inicio_2) == 1: #Ver el listado de los registros, incluido el nuevo.
                leer(productos)
                muest = input("\nQué desea realizar ahora? \n1 Volver al menú. \n2 Salir de la aplicación \nPor favor, elegir un número. ")
                if int(muest) == 1: #Volver al menú, despues de ver el listado de los registros (incluyendo al nuevo)
                    print("Volviendo al menú principal.")
                    print()
                elif int(muest) == 2:
                    print()
                    print("Saliendo de la aplicación") #Salir de la aplicacion,, despues de ver el listado de los registros (incluyendo al nuevo)
                    flag = False

            
            

        elif int (inicio) == 5:
            print()
            print("Saliendo de la aplicación.")
            flag = False
    
menu_de_inicio ()
print("Fin de proceso.")