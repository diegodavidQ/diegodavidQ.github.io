
texto = "texto de ejemplo para el curso de Python 3"

#Primera letra del string en mayúscula
#capitalize()
esultado = texto.capitalize()
#print(resultado)

#Intercambio de minúsculas a mayúsculas y viceversa
#swapcase()
resultado = texto.swapcase()
#print(resultado)

#Todo a mayúsculas
#upper()
resultado = texto.upper()
#print(resultado)

#Todo a minúsculas
#lower()
resultado = texto.lower()
#print(resultado)

##################
#Preguntar si está el mayúsculas
#isupper()
#print("¿Está en mayúsculas?: ",resultado.isupper())

#Preguntar si está el minúsculas
#islower()
#print("¿Está en minúsculas?: ",resultado.islower())

#Formato de título
#title()
resultado = texto.title()
#print("Formato título: ",resultado)

#Remplazar string
resultado = texto.replace("Python", "javaScrit")
#print(resultado)

#Sin espacios al inicio o final
texto2 = " curso de Python  "
resultado = texto2.strip()
#print("["+ resultado +"]")

####################

#Remplazo 
#método 1
curso = "Python"
version = "3"
resultado = "Curso de %s %s" %(curso, version)
print(resultado)

#método 2
resultado = "Curso de {} {}".format(curso, version)
print(resultado)

#método 3
resultado = "Curso de {a} {b}".format(a=curso, b=version)
print(resultado)

