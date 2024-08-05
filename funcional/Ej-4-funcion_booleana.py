"""Escribir una función que reciba otra función booleana y una lista, 
y devuelva otra lista con los elementos de la lista que devuelvan 
True al aplicarles la función booleana.
"""

def par(num: int):
    if (num % 2 == 0):
        return True
    

def capicua(num):
    comp = str(num)
    if (comp == comp[::-1]):
        return True

def true_element(function, list):
    list_of_true = []

    for element in list:
        if function(element):
            list_of_true.append(element)
    
    return list_of_true



print(true_element(par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(true_element(capicua, [1331, 4004, 383, 10301, 11311, 109231, 4324, 31231]))