# Escribir una función que convierta un número decimal en binario 
# y otra que convierta un número binario en decimal.


""" Primera versión
def decimal_a_binario(num):
    resultado= ""
    decimal = num
    while decimal > 0:
       residuo = decimal % 2
       resultado = resultado + str(residuo)
       decimal = decimal // 2
    return resultado[::-1]
"""
# Versión refactorizada 
def decimal_a_binario(decimal):
    resultado= ""
    while decimal > 0:
       resultado = str(decimal % 2) + resultado
       decimal = decimal // 2    
    return resultado



def binario_a_decimal(binario):
    resultado = 0
    for posicion, numero in enumerate(str(binario)[::-1]):
        if numero == '1':
            resultado += 2 ** posicion
    return resultado

"""
La forma factorizada de binario_a_decimal podría ser:
    def binario_a_decimal(binario):
        return sum(int(numero) * (2 ** posicion) for posicion, numero in enumerate(str(binario)[::-1]))

Ambas formas son correctas, pero esta versión refactorizada puede ser un poco más tediosa de entender

"""


print(decimal_a_binario(25))
print(binario_a_decimal(11001))