from Validaciones import validar_num,validacion_2dig, validar_codigo, validar_4dig_codigo
def eliminar (lista, dicc):
    flag = True
    while flag == True:
        menu= "Ingrese el código que quiere eliminar: "
        codigo_eliminar = (input(menu))
        while validar_num (codigo_eliminar) == False:
            codigo_eliminar = (input(menu))
        while validar_4dig_codigo (codigo_eliminar) == False:
            print()
            codigo_eliminar = (input(menu))
            while validar_num (codigo_eliminar) == False:
                codigo_eliminar = (input(menu))

        validacion, posicion = validar_codigo (lista,codigo_eliminar)
        if validacion == False:
            print("No se ha podido encontrar ese código, ingrese otro.")
            print()
        if validacion == True:
            print()
            print("Información del código eliminado:")
            print(lista[posicion])#Lo imprimo para que el usuario vea lo que hay en la fila
            print(f"En él se habían realizado {dicc[codigo_eliminar]} ventas.")

            lista.pop(posicion)
            del dicc[str (codigo_eliminar)]
            print()
            menu2 = "Desea eliminar otro código? \n1 Sí \n2 No \nPor favor, elegir una opción: "
            preg = (input(menu2))
            while validar_num (preg) == False:
                preg = (input(menu2))
            #Validación de número.
            while validacion_2dig(preg) == False:
                print()
                preg = (input(menu2))
                while validar_num (preg) == False:
                    preg = (input(menu2))
                
            if int (preg) == 2:
                flag = False
    return lista, dicc