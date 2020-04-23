def  iniciar_list(lista):

    def reproducir(): #solo se puede llamar dentro de la funcion iniciar_list()
        #nonlocal es para modificar la variable
        nonlocal lista
        lista.append('track 5')
        for val in lista:
            print(val)
    
    reproducir()

lista = ['track 1', 'track 2', 'track 3', 'track 4', 'track 5']

iniciar_list(lista)


