from Validaciones import validar_num, validar_4dig_codigo, validar_codigo, validar_letra, validar_let
def crear (lista, dicc):
    menu = "Ingresar cantidad de productos que quiere agregar al nuevo listado: "
    num=(input(menu))
    while validar_num (num) == False:
        num=(input(menu))
    j = 0
    while j<int(num): 
        menu2 = "Ingresar número de código del nuevo producto: "
        codigo= (input(menu2))
        while validar_num (codigo) == False:
            codigo= (input(menu2))
        while validar_4dig_codigo (codigo) == False:
            print()
            codigo= (input(menu2))
            while validar_num (codigo) == False:
                codigo= (input(menu2))
        validacion, posicion = validar_codigo (lista,codigo)
        
        if validacion == True:
            print("El código seleccionado ya está en uso, por favor, ingresar uno nuevo.")
        if validacion == False:
            menunombre = "Ingresar nombre de nuevo producto: "
            nomb= (input(menunombre))
            while validar_letra (nomb) == True:
                nomb= (input(menunombre))
            while validar_let (nomb) == False:                                                
                nomb= (input(menunombre))
                while validar_letra (nomb) == True:
                    nomb= (input(menunombre))

            prec= (input("Ingresar precio del nuevo producto: "))
            while validar_num (prec)== False:
                prec = (input("Ingresar precio del nuevo producto: "))
            
            ventas_realizadas = input("Ingresar cantidades vendidas de dicho producto: ")
            while validar_num (ventas_realizadas) == False:
                ventas_realizadas = (input("Ingresar cantidades vendidas de dicho producto: "))
            
            dicc[str (codigo)] = ventas_realizadas                    

            lista.append([codigo,nomb,prec])
            print()
            j += 1 
    return lista, dicc