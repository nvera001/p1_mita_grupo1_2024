
def leer (lista):
    print("Aquí tienes la lista de los productos, con su respectivo código y precio.")
    #Se recortan los nombres de los productos a un máximo de 8 caracteres.
    productos_recortados = [[numero, nombre[:12], precio] for numero, nombre, precio in lista]
    #Lista ordenada descendente (valor de los productos) en caso de repetir, por codigo (ascendente)
    productos_ordenados = sorted(productos_recortados, key=lambda x: (str(x[1]), -x[0]))
    #Asignación para poder mostrar las listas con encabezados.
    numero= "Código"
    nombre= "Producto"
    precio= "Valor"
    # Imprimir la lista ordenada con formato de f-strings
    print(f"|{numero:>6}| |{nombre:<12}| |{precio:>6}|")
    print("-" * 30)
    for numero, nombre, precio in productos_ordenados:
        print(f"|{numero:^6}| |{nombre:^12}| |{precio:^6}|")
    
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
    

def actualizar (lista):
    flag = True
    while flag == True:
        print()
        flag_2 = True
        pos = 0
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el código que quiere actualizar: "))
            i = 0
            while i<(len(lista)) and flag_2 == True:
                if lista[i][0] == legajo_actualizar:
                    flag_2 = False
                    pos = i
                i += 1
            if flag_2 == True:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
                print()
                print("Este es el legajo que va a actualizar: ")
                print(lista[pos])#Lo imprimo para que el usuario vea lo que hay en la fila
                nom = str (input("Ingresar el nombre del nuevo producto: "))
                prec = int (input("Ingresar precio del nuevo producto: "))
                
                for producto in lista:
                    if producto[0] == lista[pos][0]:
                        producto[1] = nom  # Cambia el nombre
                        producto[2] = prec               # Cambia el precio                
                print()
                print("Legajo actualizado")
                print(lista[pos])
                print()
                preg = int (input("Desea actualizar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                if preg == 2:
                    flag = False
    return lista

    
def eliminar (lista):
    flag = True
    while flag == True:
        print()
        flag_2 = True
        pos = 0
        while flag_2 == True:
            legajo_eliminar = int(input("Ingrese el código que quiere actualizar: "))
            i = 0
            while i<(len(lista)) and flag_2 == True:
                if lista[i][0] == legajo_eliminar:
                    flag_2 = False
                    pos = i
                i += 1
            if flag_2 == True:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
                print()
                print("Este es el legajo que va a eliminar: ")
                print(lista[pos])#Lo imprimo para que el usuario vea lo que hay en la fila
                lista.pop(pos)
                print()
                preg = int (input("Desea eliminar otro legajo? \n1 Sí \n2 No \nPor favor, elegir una opción: "))
                if preg == 2:
                    flag = False
