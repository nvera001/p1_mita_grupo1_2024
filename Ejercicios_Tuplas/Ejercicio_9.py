diccionario={
    'nombre':'Andres',
    'apellido':'Cedeño',
    'key':250,
    'dni':19125758
}
Claves=['nombre','dni']

def eliminarclaves(diccionario,claves):
    cont=0
    print(f"{diccionario}\n")
    for i in claves:
        if i in diccionario:
            diccionario.pop(i)
            cont+=1
        
    return cont, diccionario
    
print(eliminarclaves(diccionario,Claves))