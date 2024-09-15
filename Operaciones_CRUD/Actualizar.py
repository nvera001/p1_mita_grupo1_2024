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