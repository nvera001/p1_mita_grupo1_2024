
def validacion (cadena):
    import re
    patron = r"[a-zA-Z0-9]{3,}@uade+\.edu+\.ar" # R String --> Para que tome las secuencias de escape bien (Daba un warning)
    buscar = re.findall (patron,cadena)
    if len(buscar)==0:
        tupla = tuple (buscar)
        return tupla
    else:
        pat = "[@ .]"
        nom = re.split (pat,cadena)
        mail_dividido = nom[0], nom[1], nom[2], nom[3]
        tupla = tuple (mail_dividido)
        return tupla

print("Bienvenido a la aplicación")

flag = False
while flag == False:
    mail=input("Ingresar correo electrónico: ")
    tup = validacion (mail)
    while len(tup)==0: 
        print("Mail inválido.")
        mail=input("Ingresar correo electrónico: ")
        tup = validacion (mail)

    print()
    print("Devolución de tupla, que muestra la división de los caractéres del mail",tup)
    print()
    opcion = input("Desea seguir?  \n1 Sí. \n2 No. \nElegir una opción: ")
        
    if int (opcion) == 1:
        print("Continuará dividiendo mails.")
        print()
    else:
        print("Saliendo de la aplicación.")
        flag = True

print()
print("Fin de proceso.")
