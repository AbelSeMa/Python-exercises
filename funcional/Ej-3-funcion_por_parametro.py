"""Escribir una función que reciba otra función y 
una lista, y devuelva otra lista con el resultado de 
aplicar la función dada a cada uno de los elementos de la lista."""

def cuadrado(num):
    return num ** 2

def sumas(num: int):
    return num + (num + 1)


def par(function, list):
    return [function(elemento) for elemento in list]



print(par(cuadrado, [1, 2, 3, 4, 5]))
print(par(sumas, [1, 2, 3, 4, 5]))