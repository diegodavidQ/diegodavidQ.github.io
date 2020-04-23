def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #local

    def mostrar():
        print(mensaje)
    
    return mostrar


nueva_funcion = mostrar_mensaje("Diego david")
nueva_funcion()
