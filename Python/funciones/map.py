def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)
print(resultado)

lista_resultado = list(resultado)
print(lista_resultado)


################
#uso de map con lambda
lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)

