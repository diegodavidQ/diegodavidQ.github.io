#Tuplas
'''
Se definen a través de paréntesis
Son inmutables
'''

lista = ["elemento1", "elemento2", "elemento3"]
tupla = ("elemTupla1", "elemTupla2", "elemTupla3", "elemTupla4" )

#Convertir tupla a lista
nueva_lista = list(tupla)
print("Nueva lista: ", nueva_lista)

#Convertir lista a tupla
nueva_tupla = tuple(lista)
print("Nueva tupla: ", nueva_tupla)

#String a lista o tupla
mensaje = "Este es un mensaje"
print("String a lista: ", list(mensaje))
print("String a tupla: ", tuple(mensaje))
