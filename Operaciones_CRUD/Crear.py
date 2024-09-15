from Validaciones.Validaciones import validar_num, validar_4dig_legajo, validar_legajo, validar_letra, validar_let
def crear (lista):
    num=(input("Ingresar cantidad de productos que quiere agregar al nuevo listado: "))
    while validar_num (num) == False:
        num=(input("Ingresar cantidad de productos que quiere agregar al nuevo listado: "))
    j = 0
    while j<int(num): 
        codigo= (input("Ingresar número de código del nuevo producto: "))
        while validar_num (codigo) == False:
            codigo= (input("Ingresar número de código del nuevo producto: "))
            while validar_4dig_legajo (codigo) == False:
                print()
                codigo= (input("Ingresar número de código del nuevo producto: "))
                while validar_num (codigo) == False:
                    codigo= (input("Ingresar número de código del nuevo producto: "))
        validacion, posicion = validar_legajo (lista,codigo)
        if validacion == True:
            print("El código seleccionado ya está en uso, por favor, ingresar uno nuevo.")
        if validacion == False:
            print()
            nomb= (input("Ingresar nombre de nuevo producto: "))
            while validar_letra (nomb) == True:
                nomb= (input("Ingresar nombre de nuevo producto: "))
            while validar_let (nomb) == False:                                                
                nomb= (input("Ingresar nombre de nuevo producto: "))
                while validar_letra (nomb) == True:
                    nomb= (input("Ingresar nombre de nuevo producto: "))

            prec= (input("Ingresar precio del nuevo producto: "))
            while validar_num (prec)== False:
                prec = (input("Ingresar precio del nuevo producto: "))

            lista.append([codigo,nomb,prec])
            print()
            j += 1 
    