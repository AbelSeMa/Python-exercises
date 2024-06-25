# Escribir una función que reciba una muestra de números en una lista 
# y devuelva otra lista con sus cuadrados.

def cuadrados(lista: list):
    return [x**2 for x in lista] 

print(cuadrados([1, 3, 5]))