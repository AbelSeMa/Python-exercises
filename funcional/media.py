# Escribir una función que reciba una muestra de números en una lista 
# y devuelva su media.


def media(lista: list):
    return sum(lista) / len(lista)


print(media([2, 5, 7, 10, 123, 5453]))