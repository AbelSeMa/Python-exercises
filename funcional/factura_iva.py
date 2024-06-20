### Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def sin_iva(cantidad: int, iva: int = 21):
    total = (cantidad * iva) / 100 + cantidad
    return str(total) + "€"

print(sin_iva(2342, 10))