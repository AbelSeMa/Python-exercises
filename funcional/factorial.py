### Escribir una función que reciba un número entero positivo
#  y devuelva su factorial.

def factorial(num: int):
    acc = 1
    for x in range(1,num + 1):
        acc *= x
    return acc


print(factorial(-5))