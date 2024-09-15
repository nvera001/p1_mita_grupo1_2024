from Validaciones.Validaciones import validar_num,validar_legajo,validar_4dig_legajo, validar_let,validacion_2dig,validar_letra
def actualizar (lista):
    flag = True
    while flag == True:
        flag_2 = True
        pos = 0
        while flag_2 == True:
            legajo_actualizar = (input("Ingrese el código que quiere actualizar: "))

            while validar_num (legajo_actualizar) == False:
                legajo_actualizar = (input("Ingrese el código que quiere actualizar: "))
            while validar_4dig_legajo (legajo_actualizar) == False:
                print()
                legajo_actualizar = (input("Ingrese el código que quiere actualizar: "))
                while validar_num (legajo_actualizar) == False:
                    legajo_actualizar = (input("Ingrese el código que quiere actualizar: "))

            
            validacion, posicion = validar_legajo (lista,legajo_actualizar)            
            if validacion == False:
                print("No se ha podido encontrar ese código, ingrese otro.")
                print()
            if validacion == True:
                flag_2 = False
                print()
                print("Este es el código que va a actualizar: ")
                print(lista[posicion])#Lo imprimo para que el usuario vea lo que hay en la fila
                print()
                segur = (input("Está usted seguro que lo quiere actualizar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                while validar_num (segur) == False:
                    segur = (input("Está usted seguro que lo quiere actualizar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                while validacion_2dig (segur) == False:
                    print()
                    segur = (input("Está usted seguro que lo quiere actualizar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                    while validar_num (segur) == False:
                        segur = (input("Está usted seguro que lo quiere actualizar? \n1 Sí \n2 No \nPor favor, elegir un número: "))
                
                if int(segur) == 1:
                    nom = (input("Ingresar el nombre del nuevo producto: "))
                    while validar_letra (nom) == True:
                        nom = (input("Ingresar el nombre del nuevo producto: "))
                    while validar_let (nom) == False:                                                
                        nom = (input("Ingresar el nombre del nuevo producto: "))
                        while validar_letra (nom) == True:
                            nom = (input("Ingresar el nombre del nuevo producto: "))

                            
                    prec = (input("Ingresar precio del nuevo producto: "))
                    while validar_num (prec)== False:
                        prec = (input("Ingresar precio del nuevo producto: "))
                    
                    for producto in lista:
                        if producto[0] == lista[posicion][0]:
                            producto[1] = nom  # Cambia el nombre
                            producto[2] = prec               # Cambia el precio                
                    print()
                    print("Código actualizado")
                    print(lista[posicion])
                    print()
                    preg = (input("Desea actualizar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                    while validar_num (preg) == False:
                        preg = (input("Desea actualizar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                    #Validación de número.
                    while validacion_2dig(preg) == False:
                        print()
                        preg = (input("Desea actualizar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                        while validar_num (preg) == False:
                            preg = (input("Desea actualizar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                    
                    if preg == 2:
                        flag = False
                if int(segur) == 2:
                    print()
                    print("Volviendo al menú anterior para que pueda ingresar su código correspondiente")
                    print()    
    return lista