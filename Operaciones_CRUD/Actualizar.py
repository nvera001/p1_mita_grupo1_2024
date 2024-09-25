from Validar.Validaciones import validar_num,validar_codigo,validar_4dig_codigo, validar_let,validacion_2dig,validar_letra
def actualizar (lista, dicc):
    flag = True
    while flag == True:
        menu = "Ingrese el código que quiere actualizar: "
        codigo_actualizar = (input(menu))
        while validar_num (codigo_actualizar) == False:
            codigo_actualizar = (input(menu))
        while validar_4dig_codigo (codigo_actualizar) == False:
            print()
            codigo_actualizar = (input(menu))
            while validar_num (codigo_actualizar) == False:
                codigo_actualizar = (input(menu))
        
        validacion, posicion = validar_codigo (lista,codigo_actualizar)            
        if validacion == False:
            print("No se ha podido encontrar ese código, ingrese otro.")
            print()
        if validacion == True:
            flag_2 = False
            print()
            print("Este es el código que va a actualizar: ")
            print(lista[posicion])#Lo imprimo para que el usuario vea lo que hay en la fila
            print(f"En él se han realizado {dicc[codigo_actualizar]} ventas.")
            
            print()
            menu2 = "Ingresar el nombre del nuevo producto: "
            nom = (input(menu2))
            while validar_letra (nom) == True:
                nom = (input(menu2))
            while validar_let (nom) == False:                                                
                nom = (input(menu2))
                while validar_letra (nom) == True:
                    nom = (input(menu2))

            prec = (input("Ingresar precio del nuevo producto: "))
            while validar_num (prec)== False:
                prec = (input("Ingresar precio del nuevo producto: "))
            
            ventas_realizadas = input("Ingresar cantidades vendidas de dicho producto: ")
            while validar_num (ventas_realizadas) == False:
                ventas_realizadas = (input("Ingresar cantidades vendidas de dicho producto: "))
            
            dicc[str (codigo_actualizar)] = ventas_realizadas                    

            for producto in lista:
                if producto[0] == lista[posicion][0]:
                    producto[1] = nom  # Cambia el nombre
                    producto[2] = prec               # Cambia el precio                
            print()
            print("Código actualizado")
            print(lista[posicion])
            print(f"En él se han realizado {dicc[codigo_actualizar]} ventas.")
            print()
            
            print()
            menu3 = "Desea actualizar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "
            preg = (input(menu3))
            while validar_num (preg) == False:
                preg = (input(menu3))
            #Validación de número.
            while validacion_2dig(preg) == False:
                print()
                preg = (input(menu3))
                while validar_num (preg) == False:
                    preg = (input(menu3))
            
            if int (preg) == 2:
                flag = False
    return lista, dicc