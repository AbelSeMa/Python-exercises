"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o 
el IVA a los productos de la cesta y devolver el precio final de la cesta.
"""

def descuento(precio: float, descuento: int):
    return precio - (precio * (descuento / 100))

def iva(precio: float, iva: int):
 return precio + (precio * (iva / 100))

def cesta(dicc: dict, funcion):
   total = 0
   for precio, porcentaje in dicc.items():
      total += funcion(precio, porcentaje)
   return total




print(iva(100, 21))
print(descuento(321, 10))
print(cesta({1:4, 10:21, 77.8:21}, descuento))