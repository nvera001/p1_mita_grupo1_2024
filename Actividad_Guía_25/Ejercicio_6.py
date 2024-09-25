from Validaciones import validacion_2dig, validar_letra

import re 

def eliminacion (phrasal):
    listado_palabras = frase.split ()

    conjunto = set(listado_palabras)
    """conjunto_nuevo = conjunto.discard (".,;:!¿?()[]{}'\"-")"""
    conjunto = sorted (conjunto)
    return conjunto

print()
print("Bienvenido a la aplicación")
flag = False
while flag == False:
    frase = input ("Ingresar frase ")
    while validar_letra  (frase) == False:
        frase = input ("Ingresar frase ")

    conj = eliminacion (frase)
    print("Palabras que quedaron luego de la eliminación de repetidos: ")
    print(conj)

    print()
    opcion = input("Desea seguir?  \n1 Sí. \n2 No. \nElegir una opción: ")
    while validacion_2dig(opcion) == False: 
        opcion = input("Desea seguir?  \n1 Sí. \n2 No. \nElegir una opción: ")  
        
    if int (opcion) == 1:
        print("Continuará dividiendo mails.")
        print()
    else:
        print("Saliendo de la aplicación.")
        flag = True