class Usuario:
    
    def __init__(self, username='', correo='', nombre=''):
        #Atributos
        self.username = username
        self.correo = correo
        self.nombre = nombre

    #self hace referencia al objeto en sí
    def saluda(self):
        return"Hola soy el usuario "+ self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre


diego = Usuario("diegod", "diego@gmail.com", "Diego")
res = diego.saluda()

print(res)


