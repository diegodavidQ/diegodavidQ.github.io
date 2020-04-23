'''

'''
texto = "Curso de Python 3"

#Cantidad de caracteres con len()
resultado = len(texto)
print("Número de caracteres: ", resultado)

#Obtención de caracteres
inicial = texto[0] #inicial
final = texto[-1] #final
print("Inicial: ", inicial)
print("Final: ", final)

#Con saltos, [posición_inicial, posición_final, salto]
resultado = texto[1:15:2]
print("Con salto 2: ", resultado)
