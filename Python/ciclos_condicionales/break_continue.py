titulo = "Curso de Python 3"
texto = ""

for caracter in titulo:    
    if caracter == "o":
        continue
    elif caracter == "P":
        break
    texto +=caracter
    print(caracter)

print(texto)

