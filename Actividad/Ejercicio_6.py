from Validar.Validaciones import validacion_2dig, validar_letra


def eliminacion (phrasal):
    listado_palabras = frase.split ()

    conjunto = set(listado_palabras)
    """conjunto_nuevo = conjunto.discard (".,;:!¿?()[]{}'\"-")"""
    conjunto_ordenado = sorted(conjunto, key=lambda x: -len(x))
    return conjunto_ordenado

print()
print("Bienvenido a la aplicación")
flag = False
while flag == False:
    frase = input ("Ingresar frase: ")
    while validar_letra  (frase) != False:
        frase = input ("Ingresar frase ")

    conj = eliminacion (frase)
    print()
    print("Palabras que quedaron luego de la eliminación de repetidos: ")
    print(conj)

    print()
    opcion = input("Desea seguir?  \n1 Sí. \n2 No. \nElegir una opción: ")
    while validacion_2dig(opcion) == False: 
        opcion = input("Desea seguir?  \n1 Sí. \n2 No. \nElegir una opción: ")  
        
    if int (opcion) == 1:
        print("Continuará eliminando repetidos.")
        print()
    else:
        print("Saliendo de la aplicación.")
        flag = True
        
print()
print("Fin de proceso.") 