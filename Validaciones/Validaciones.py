import re
def validar_num (car):    
    if car.isnumeric()==False:
        print()
        print("Por favor, ingresar un número.")
        print()
    return car.isnumeric()

def validar_letra (car):
    if car.isnumeric () == True:
        print()
        print("Por favor, no ingresar números.")
        print()
    return car.isnumeric()

def validacion_2dig (texto):                 
    patron = "[1-2]{1}"
    if re.match(patron,texto) == None:
        print("Por favor, ingresar un numero válido.")
        return False

def validar_legajo (list, legajo):
    i = 0
    while i<(len(list)):
        if list[i][0] == int (legajo):
            pos = i
            return True, pos
        i += 1
    return False,i

def validar_4dig_legajo (car):
    patron = "^[0-9]{4}$"
    if re.match(patron,car) == None:
        print("Por favor, ingresar un numero válido.")
        return False

def validar_let (car):
    patron = "^[A-Z][a-z]+$"
    if re.match (patron,car) == None:
        print("Por favor, al momento de ingresar el nombre del producto, comenzar con una letra mayúscula y no incluir números.")
        return False
    
def  validacion_5dig (texto):
    patron = "[1-5]{1}"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False
def validacion_3dig (texto):                 
    patron = "[1-3]{1}"
    if re.match(patron,texto) == None:
        print("Por favor, ingresar un numero válido.")
        return False
