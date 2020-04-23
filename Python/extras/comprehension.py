'''
lista = []

for x in range(0,101):
    lista.append(x)
'''
#---------------------------------------------#
estructura = [x for x in range(0,101) ]
print(estructura)

#---------------------------------------------#
tupla = tuple((x*x for x in range (0,10)))
print(tupla)

#---------------------------------------------#
tupla2 = tuple((x for x in range (0,100) 
                    if x % 2 == 0
                        if x<50))
print(tupla2)

#---------------------------------------------#
diccionario = { indice:valor 
                for indice, valor in enumerate(tupla2) }

print(diccionario)