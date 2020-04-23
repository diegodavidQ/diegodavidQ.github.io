class Animal:
    def comer(self):
        print("comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Este es un método de Animal")

#--------------------------------------#
class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_adopcion = fecha
    
    def comun(self):
        print("Este es un método de Mascota")
#--------------------------------------#

class Perro(Animal, Mascota): #Animal es clase padre
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("Ladrando")
    
    def comun(self):
        print("Este es un método de Perro")
#--------------------------------------#

class Gato(Animal, Mascota):
    def ronroneo(self):
        print("ronroneo")
#--------------------------------------#

bethoven = Perro("Bethoven")
bethoven.fecha_adopcion("Hoy")
print(bethoven.fecha_adopcion)
bethoven.ladrar()
bethoven.comer()

brote = Gato()
brote.ronroneo()

#método común con las herencias
bethoven.comun()



