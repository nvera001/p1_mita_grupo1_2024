import random
def crear_matriz (n,m):
    """
    pre: recibe n y m. Donde n: filas y M: columnas.
    pos: devuelve una matriz de NxM creada con ceros.
    """
    return [[0]*m for fil in range (n)]

def llenar_matriz (m):
    """
    pre: recibe una matriz ya creada.
    pos: llena la matriz con valores aleatorios entre 1 y 10    
    """
    filas = len(m) #cantidad de filas
    columnas= len(m[0]) #cantidad de columnas
    for fil in range (filas):
        for col in range (columnas):
            num_aleatorio = random.randint (1,9)
            m[fil][col]= num_aleatorio
    return m
   
def mostrar_matriz (matriz, estudiantes, materias):
    print("       " + "  ".join(materias))
    
    for i, fila in enumerate(matriz):
        print(f"{estudiantes[i]:<10} " + "  ".join(str(calificacion) for calificacion in fila))
        
    
def calcular_promedio_estudiantes(matriz,estudiantes,materias):
    filas = len(matriz) #cantidad de filas
    columnas= len(matriz[0]) #cantidad de columnas
    for fil in range (filas):
        suma=0
        for col in range (columnas):
            suma += matriz[fil][col]
        prom = suma / len(materias)
        print("El promedio de",estudiantes[fil],"fue de ",prom)


def calcular_promedio_materia(matriz,estudiantes,materias):
    filas = len(matriz) #cantidad de filas
    columnas= len(matriz[0]) #cantidad de columnas
    for col in range (columnas):
        suma=0
        for fil in range (filas):
            suma += matriz[fil][col]
        prom = suma / len(estudiantes)
        print("El promedio de",materias[col],"fue de ",prom)

print
lista_estudiantes = ["Juan","Ana","Nicolas","Martin","Ariel"] 
lista_materias = ["M", "H", "C", "I","B","T","G"] 
a=crear_matriz(len(lista_estudiantes),len(lista_materias))
b=llenar_matriz(a)
print()
mostrar_matriz(b,lista_estudiantes,lista_materias)

print()
calcular_promedio_estudiantes(b,lista_estudiantes,lista_materias)
print()
calcular_promedio_materia(b,lista_estudiantes,lista_materias)
