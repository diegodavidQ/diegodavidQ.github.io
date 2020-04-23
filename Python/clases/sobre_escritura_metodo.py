class Animal:
    def comer(self):
        print("comiendo")

    def dormir(self):
        print("Durmiendo")

#--------------------------------------#
class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_adopcion = fecha
    
    def comun(self):
        print("Este es un método de Mascota")
#--------------------------------------#

class Perro(Animal, Mascota): 
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("Ladrando")

    #sobre escritura del método dormir
    def dormir(self):
        print(self.nombre, "esta durmiendo!")
        Animal.dormir(self) #si se desea agregar más funcionalidaddes
        print("No molestar")
#--------------------------------------#

bethoven = Perro("Bethoven")
bethoven.dormir()



