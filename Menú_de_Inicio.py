from Operaciones_CRUD.Actualizar import actualizar
from Operaciones_CRUD.Crear import crear
from Operaciones_CRUD.Eliminar import eliminar
from Operaciones_CRUD.Leer import leer
from Validaciones.Validaciones import validacion_5dig, validar_num
from Matriz_y_Diccionario.Matriz_Productos import productos
from Matriz_y_Diccionario.Diccionario_Productos import cantidades_vendidas
print()
#Se define la lista de los productos.

def menu_de_inicio():
    print
    print("Bienvenido a la aplicación del supermercado.")
    flag = True
    while flag!=False:
        menu = "\nQué desea realizar? \n1 Listado de productos.\n2 Agregar nuevos registros a la lista.\n3 Editar un registro de la lista. \n4 Eliminar un registro de la lista. \n5 Salir de la aplicación. \nElija un numero: "
        inicio=input(menu) #Menú de inicio.
        while validar_num(inicio) == False:
            inicio=input(menu) #Menú de inicio.
        while validacion_5dig (inicio)== False:
            inicio=input(menu) #Menú de inicio.
            while validar_num(inicio) == False:
                inicio=input(menu) #Menú de inicio.
        
        if int (inicio)==1: #Muestra de registros.
            print()
            leer (productos, cantidades_vendidas)
            print()
       
        elif int (inicio) == 2: #Agregar nuevos registros.
            print()
            crear(productos, cantidades_vendidas)
            print()

        elif int (inicio) == 3: #Editar un registro de la lista.
            print()
            actualizar (productos, cantidades_vendidas)
            print()

        elif int (inicio) == 4: #Eliminar uno de los registros.
            print()
            eliminar(productos, cantidades_vendidas)
            print()

        elif int (inicio) == 5: #Sale de la aplicación.
            flag = False
    
menu_de_inicio ()
print()
print("Fin de proceso.")