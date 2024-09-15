def leer (lista):
    print("Aquí tienes la lista de los productos, con su respectivo código y precio.")
    #Se recortan los nombres de los productos a un máximo de 8 caracteres.
    productos_recortados = [[numero, nombre[:12], precio] for numero, nombre, precio in lista]

    # Aplicamos un descuento del 10% a todos los productos
    productos_con_descuento = list(map(lambda x: [x[0], x[1], x[2] * 0.9], productos_recortados))

    # Luego, aplicamos el ordenamiento a la lista con descuento
    productos_ordenados = sorted(productos_con_descuento, key=lambda x: (x[2], str(x[1]), -x[0]))

    #Asignación para poder mostrar las listas con encabezados.
    numero= "Código"
    nombre= "Producto"
    precio= "Valor"
    # Imprimir la lista ordenada con formato de f-strings
    print(f"|{numero:>6}| |{nombre:<12}| |{precio:>7}|")
    print("-" * 33)
    for numero, nombre, precio in productos_ordenados:
        print(f"|{numero:^6}| |{nombre:^12}| |{precio:^7}|")