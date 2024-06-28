###
# Crea una función que determine si un año es bisiesto

def bisiestos(anyo: int):
    if (anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)):
        return "El año es bisiesto"
    else:
        return "El año no es bisiesto"


print(bisiestos(2012))
print(bisiestos(1997))
print(bisiestos(1543))
print(bisiestos(2056))
print(bisiestos(2145))