def suma(*args):
    res = 0
    for arg in args:
        res += arg
    return res

def resta(*args):    
    #Resta al primer número todos los demás 
    res = args[0]
    args2=args[1::]
    for arg in args2:        
        res -= arg
    return res

def multiplicacion(*args):
    res=1
    for arg in args:
        res *= arg
    return res

def división(*args):
    res = args[0]
    args2=args[1::]
    for arg in args2:
        if arg == 0 or arg == 0.0:
            return print("No es posible dividir para cero.")
            break
        res = res / arg
    return res





