# Escribir una función que reciba una muestra de números en una lista 
# y devuelva un diccionario con su media, varianza y desviación típica.
import math

def operaciones(lista):
    media = sum(lista) / len(lista)
    cuadrados = [x**2 for x in lista]
    suma_cuadrados = sum(cuadrados)
    varianza = suma_cuadrados / len(lista)
    desviacion = math.sqrt(varianza)

    return {"Media":media,
            "Varianza":varianza,
            "Desviación típica": desviacion}


print(operaciones([1, 2, 4, 6]))