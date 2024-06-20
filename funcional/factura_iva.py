def sin_iva(cantidad: int, iva: int = 21):
    print(str((cantidad * iva) / 100 + cantidad) + "€")

sin_iva(2342, 10)