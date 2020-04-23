'''
El separador por default es el espacio,
dentro de split() se podría colocar el separador
'''
lenguajes = "Python; Java; PHP; Kotlin; C#; C++; JavaScript"

separador = "; "
resultado = lenguajes.split(separador)
print("Lista generada con split: ", resultado)

'''
Con join() se genera un string a partir de una lista 
'''
nuevo_string = separador.join(resultado)
print("String generado con join: ",nuevo_string)

#Si existe saltos de línea
texto = """Texto con
saltos
de
línea"""
resultado = texto.splitlines()
print("Lista a partir de texto con saltos de línea: ", resultado)
