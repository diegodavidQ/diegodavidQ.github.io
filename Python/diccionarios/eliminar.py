diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5}

print(diccionario)
print("Número de elementos: ", len(diccionario))

#método 1
del diccionario["a"]
print(diccionario)

#método 2
valor = diccionario.pop("b")
print("valor eliminado: ", valor)
print(diccionario)

#método 3
# eliminar todo el diccionario
diccionario = {}
print("Número de elementos: ", len(diccionario))

#método 4
diccionario.clear()
print(diccionario)