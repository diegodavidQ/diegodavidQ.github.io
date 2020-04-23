#primera forma de importar un módulo
'''
import calculadora

resultado = calculadora.suma(20,4,2)
print(resultado)

'''
#---------------------------------#
#segunda forma de importar un módulo
from calculadora import (multiplicacion,
                        resta,
                        suma,
                        división)

resultado = multiplicacion(20,4,2)
print(resultado)

resultado = resta(100, 20, 30)
print(resultado)

