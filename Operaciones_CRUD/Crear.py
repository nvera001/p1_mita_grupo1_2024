def crear (lista):
    num=int (input("Ingresar cantidad de productos que quiere agregar al nuevo listado: "))
    j = 0
    while j<num: 
        codigo=int (input("Ingresar número de código del nuevo producto: "))
        flag = False
        while flag == False:
            i = 0
            while i< (len(lista)):
                if lista [i][0] == codigo:
                    print("El código seleccionado ya está en uso, por favor, ingresar uno nuevo.")
                    codigo=int (input("Ingresar número de código del nuevo producto: "))
                i += 1
            flag = True            

        nomb=str (input("Ingresar nombre de nuevo producto: "))
        prec=int (input("Ingresar precio del nuevo producto: "))
        lista.append([codigo,nomb,prec])
        print()
        j += 1 
    