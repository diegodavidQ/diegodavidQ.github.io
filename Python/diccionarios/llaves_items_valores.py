#Llaves, ítems y valores
diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5}

#obtener llaves
resultado = diccionario.keys() #objeto
#print(resultado)
resultado = tuple(resultado) #tupla
#print(resultado)

#obtener valores
resultado = diccionario.values() #objeto
#print(resultado)

#obtener los items
resultado = diccionario.items()
resultado = list(resultado)
print(resultado)

