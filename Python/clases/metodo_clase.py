#se pueden llamar sin la necesidad de realizar una instancia de la clase
class Circulo:
    pi = 3.14159265

    @classmethod
    def area(cls, radio): #cls hace referencia a la clase
        return cls.pi * radio**2
    
resultado = Circulo.area(10)
print(resultado)
