calificacion = 10
color = 'rojo'

if calificacion >= 7:
    color = 'verde'

print(calificacion, color)

#reduccion de codigo
calificacion = 6
color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion, color)

