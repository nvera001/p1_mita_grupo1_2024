lista=[]
def main():
    intentos=0
    while True:
        try:
            ing=int(input("Ingresar el dígito solicitado"))
            if ing!=-1:
                lista.append(ing)
            else:
                break
        except(ValueError):
            print("Ingrese un valor adecuado")
            continue
    print(lista)
    while True:
        if intentos==3:
            print("Ha fallado demasiadas veces, cerrando programa.")
            break
        try:
            busc=int(input("Ingrese el valor que desea buscar: "))
            lista.index(busc)
        except(ValueError):
            print("Ingrese un valor adecuado")
            intentos+=1
            continue
        else:
            print("El valor esta en la lista")
            break

main()