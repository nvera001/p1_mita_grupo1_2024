import random

def main():
    num=random.randint(1,500)
    print(num)
    intentos=0
    while True:
        try:
            busc=int(input("Ingrese el número que supone es: \n"))
        except (ValueError):
            print("Ingrese un valor adecuado")
            intentos+=1
            continue
        finally:
            if busc<num:
                print("El número ingresado es mas grande que el que buscas.\n")
                intentos+=1
                continue
            elif busc>num:
                print("El número que buscas es mas pequeño que el indicado.\n")
                intentos+=1
                continue
            else:
                break
    print(f"¡Felicidades, encontraste el número! Te tomó {intentos+1} intentos")

main()