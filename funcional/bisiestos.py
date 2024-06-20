def bisiestos(anyo: int):
    if (anyo % 4 == 0 and anyo % 100 != 0):
        print("El año es bisiesto")
    elif (anyo % 100 == 0 and anyo % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")


bisiestos(2012)
bisiestos(1997)
bisiestos(1543)
bisiestos(2056)
bisiestos(2145)