#crear secuencia de números

for valor in range(10):
    print(valor)


for valor in range(1, 20, 2):
    print(valor)

#recorrer lista
lista = [1,2,3,4,5,6,7]

for indice in range ( len(lista) ):
    print("indice:", indice, "valor:", lista[indice] )

#recorrer lista
for indice, valor in enumerate(lista):
    print("indice:", indice, "valor:", valor)

