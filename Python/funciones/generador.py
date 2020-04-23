def tabla_multiplicar(numero, maximo=12):
    for posicion in range(1, maximo+1):
        yield numero * posicion, numero, posicion #yield retorna cada posicion

for resultado, numero, posicion in tabla_multiplicar(9):
    print (numero, "*", posicion, "=", resultado)



