texto = "Texto ejemplo para uso de búsquedas en python 3"

#contar cuantas veces aparece
resultado = texto.count("para")
print(resultado)

#in
resultado = "ejemplo" in texto
print("¿Se encuentra \"ejemplo\" en el texto? ",resultado)


#extraer cadena
resultado = texto.find("python")
resultado = texto[resultado: resultado+len("python")]
print(resultado)


#si se encuentra al inicio
resultado = texto.startswith("Texto")

#si se encuentra al final
resultado = texto.endswith("3")


