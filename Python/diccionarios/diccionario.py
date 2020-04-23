"""
Clave - Valor
mutables
"""

#Definir diccionario
diccionario = {}
diccionario2 = dict()

#{ llave: valor}
diccionario = {"numero": 55}
diccionario = {"numero": 55, "descuento":True, "subtotal": 15}

#######
diccionario = {"clave1": 55, 10: "Curso de Python", (1,5,8): True}

#Agregar nueva llave-valor
diccionario['usuario'] = 'Diego'

#Actualización
diccionario['usuario'] = 'David'

#Obtener valor
print(diccionario['usuario'])

#Obtener todas las claves del diccionario
diccionario = {"Diego": 1, "David": 2, "Steve": 3, "Uriel": 4}
print("claves: ", diccionario.keys())

#Obtener todos los valores
print("valores: ", diccionario.values())

#recorrer diccionario
for key, value in diccionario.items():
    print(key, value)


#################
#Método GET
#es posible colocar un valor por defecto si no exite
usuario = {
    'name': 'Diego David',
    'age': 28,
    'curso': 'Python'
}

calificaciones = usuario.get('calificaciones',[]) #si no existe retorna []
if calificaciones:

    for calificacion in calificaciones:
        print(calificacion)


###################
#De lista a diccionario
usuarios = ['Diego', 'David', 'Uriel', 'Eduardo']
diccionario = {usuario:position+1
                        for position, usuario in enumerate(usuarios)}

print(diccionario)
