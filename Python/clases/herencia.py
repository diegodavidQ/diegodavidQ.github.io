class Animal:
    def comer(self):
        print("comiendo")

    def dormir(self):
        print("Durmiendo")


class Perro(Animal): #Animal es clase padre
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("Ladrando")

class Gato(Animal):
    def ronroneo(self):
        print("ronroneo")


bethoven = Perro("Bethoven")
bethoven.ladrar()
bethoven.comer()

brote = Gato()
brote.ronroneo()
