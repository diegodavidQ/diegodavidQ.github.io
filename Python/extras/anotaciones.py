#Solamente son anotaciones no son reglas

def saludo ( nombre: str) -> str:
    return "Hola " + nombre

nombre = "Diego"
print(saludo(nombre))

def suma(num1 : int, num2 : int = 100) -> int:
    return num1 + num2

print(suma(20, 5))

