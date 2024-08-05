"""
Escribir una función reciba una lista de notas y 
devuelva la lista de calificaciones correspondientes a esas notas.
"""

def note_list(list):
    calificaciones = []
    for nota in list:
        if nota >= 9.0:
            calificaciones.append("Sobresaliente")
        elif nota >= 7.0:
            calificaciones.append("Notable")
        elif nota >= 5.0:
            calificaciones.append("Aprobado")
        else:
            calificaciones.append("Suspenso")
        
    return calificaciones


print(note_list([4.9, 5, 6, 7, 7.9, 10, 9]))