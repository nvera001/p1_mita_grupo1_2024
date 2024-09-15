from Validaciones.Validaciones import validar_num,validacion_2dig, validar_legajo, validar_4dig_legajo
def eliminar (lista):
    flag = True
    while flag == True:
        print()
        flag_2 = True
        pos = 0
        while flag_2 == True:
            legajo_eliminar = (input("Ingrese el código que quiere eliminar: "))
            while validar_num (legajo_eliminar) == False:
                legajo_eliminar = (input("Ingrese el código que quiere eliminar: "))
            while validar_4dig_legajo (legajo_eliminar) == False:
                print()
                legajo_eliminar = (input("Ingrese el código que quiere eliminar: "))
                while validar_num (legajo_eliminar) == False:
                    legajo_eliminar = (input("Ingrese el código que quiere eliminar: "))

            validacion, posicion = validar_legajo (lista,legajo_eliminar)
            if validacion == False:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
                print()
            if validacion == True:
                flag_2 = False
                print()
                print("Este es el legajo que va a eliminar: ")
                print(lista[posicion])#Lo imprimo para que el usuario vea lo que hay en la fila
                segur = (input("Está usted seguro que lo quiere eliminar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                while validar_num (segur) == False:
                    segur = (input("Está usted seguro que lo quiere eliminar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                while validacion_2dig (segur) == False:
                    print()
                    segur = (input("Está usted seguro que lo quiere eliminar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                    while validar_num (segur) == False:
                        segur = (input("Está usted seguro que lo quiere eliminar? \n1 Sí \n2 No \nPor favor, elegir un número: "))

                if int (segur) == 1:                    
                    lista.pop(posicion)
                    print()
                    preg = (input("Desea eliminar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                    while validar_num (preg) == False:
                        preg = (input("Desea eliminar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                    #Validación de número.
                    while validacion_2dig(preg) == False:
                        print()
                        preg = (input("Desea eliminar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                        while validar_num (preg) == False:
                            preg = (input("Desea eliminar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                        
                    if int (preg) == 2:
                        flag = False
                if int (segur) == 2:
                    print()
                    print("Volviendo al menú anterior para que pueda ingresar su código correspondiente")
                    print()
    return lista