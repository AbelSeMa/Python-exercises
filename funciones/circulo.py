###
# Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.


from math import pi

def area_circulo(diametro: float):
    radio = diametro / 2
    area = round(pi * radio**2, 5)
    return area

def volumen_cilindro(altura: float, diametro: float):
    area = area_circulo(diametro)
    volumen = round(area * altura, 5)
    return volumen


print("Area: " + str(area_circulo(1224242)))
print("Volumen: " + str(volumen_cilindro(10, 2)))