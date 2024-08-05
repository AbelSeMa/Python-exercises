# Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def palabrerio(cadena: str):
    puntuacion = ".,;:!¿?"
    for caracter in puntuacion:
        cadena = cadena.replace(caracter, "")

    lista_palabras = cadena.lower().split(" ")
    diccionario = {}

    for palabra in lista_palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1

    return diccionario


def palabra_repetida(diccionario):
    repeticion_alta = max(diccionario.values())
    palabras = [repeticion_alta]

    for palabra, repetecion in diccionario.items():
        if repetecion == repeticion_alta:
            palabras.insert(-1, palabra)

    return tuple(palabras)


print(palabrerio("Verde nativo, verde de nativo que sueña verde nativo verde de nativo humana"))
print(palabra_repetida(palabrerio("Verde nativo, verde de nativo que sueña verde nativo verde de nativo humana")))

"""
    *** Primera versión del ejercicio 1 ***
        Problemas encontrados: Los carácteres de puntuación se unian a la palabra. 
        En el uso de la función quedaría una lista con la palabra: verde,
        La solución pasa por eliminar todos los carácteres de puntuación.

        # Forma simplificada usando la clase Counter del módulo collections
        from collections import Counter

        def palabrerio_simple(cadena: str):
            lista_palabras_dos = cadena.lower().split(" ")
            diccionario_dos = Counter(lista_palabras_dos)

            return diccionario_dos

    *** Segunda parte del ejercicio ***
        Problemas encontrados: Cuando hay más de una palabra con la misma repeteción 
                                sólo se devolvía la ultima palabra del diccionario
        Solución: Como ya sabemos el nº máximo de repeticiones, creamos una lista con ese mismo número, 
                    y añadimos las palabras que tengan esa repetición a la lista
                    y devolvemos una tupla a partir de la lista de palabras y repeteción
"""