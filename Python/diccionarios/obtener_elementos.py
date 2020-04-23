#Obtener elementos de un diccionario
diccionario = {"a":1, "b":2, "c":3, "a":4}

resultado = diccionario["a"]
print(resultado)

#si se coloca una llave que no existe, se retorna un error
#resultado = diccionario["z"]
#print(resultado)

#para saber si una llave existe 
#in
resultado = "z" in diccionario
print(resultado)

#uso del método get
#el segundo valor se retorna cuando no existe la llave
resultado = diccionario.get("z", "No existe la llave")
print(resultado)

