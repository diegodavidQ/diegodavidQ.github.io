#Definición
def saludar(nombre="David"): #por defecto el parámetro es David
    mensaje = "Hola {}, bienvenido al curso de Python 3".format(nombre)
    print(mensaje)

#Llamada
saludar("Diego")
saludar()

###############################
#Múltiples entradas

def suma (*args):
    res = 0
    for arg in args:
        res += arg
    return res

print(suma(2,7,11,16))


def factorial(numero):
    fact=1
    for i in range(numero, 1, -1):
        fact *= i
    return fact

print("Factorial:",factorial(5))

####################################
##agrupar en diccionario
def usuarios(**kwargs):
    print(kwargs)

usuarios(a=True, b=2, c="string")


