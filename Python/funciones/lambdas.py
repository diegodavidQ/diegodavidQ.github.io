'''def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

farhrenheit = centigrados_a_farhenheit
resultado = farhrenheit(32)
print(resultado)
'''
#############################
#FUNCIONES LAMBDAS
#En una línea de código
#todas las funciones lambda retorna un valor

mi_funcion = lambda grados=0 : grados * 1.8 + 32

resultado = mi_funcion(32)
print(resultado)

'''
Estas son algunas formas en las cuales se puede crear funciones lambdas:

sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)

'''

