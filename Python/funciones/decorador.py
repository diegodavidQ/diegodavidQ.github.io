#tres funciones: a,b,c 
# a(b) -> c

def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Se puede agregar código antes")
        resultado = funcion(*args, **kwargs)
        print("Se puede agregar código después")
        return resultado

    return nueva_funcion


@decorador
def funcion_a_decorar():
    print("Esta es una funcion a decorar")

funcion_a_decorar()
print("\n")
#########################

@decorador
def suma(val1, val2):
    return val1 + val2

resultado = suma(15,8)
print(resultado)
