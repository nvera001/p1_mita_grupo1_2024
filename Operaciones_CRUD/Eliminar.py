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
