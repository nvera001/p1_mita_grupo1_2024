import math
def main():  
    while True:
        try:
            num=int(input("Ingrese un número: "))
            print(math.sqrt(num))
            
        except(ValueError):
            print("Ingrese un valor adecuado")
            continue
        else:
            break

main()