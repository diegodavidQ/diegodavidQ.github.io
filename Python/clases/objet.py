#Dos instancias de crear clase
#Ambas están heredando de la clase object

class Clase1:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self): #para no visualizar el espacio en memoria
        return self.nombre

class Clase2(object):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre


clase1 = Clase1("nombre1")
clase1.atributo2 = 17
clase2 = Clase2("nombre2")

print(clase1.__dict__) #Todos los atributos del objeto
print(clase2)
