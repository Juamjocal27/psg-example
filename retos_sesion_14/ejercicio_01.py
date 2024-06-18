"""
Un estudiante desea saber cuál es su promedio de calificaciones en la materia
de matematicas, cree una función que reciba las calificaciones como lista
y devuelva el promedio las calificaciones son 20, 40, 60, 51, 13
"""
def promedio_nota(notas):
    return sum(notas) / len(notas)

calificaciones = [20, 40, 60, 51, 13]
nota = promedio_nota(calificaciones)
print(f"Promedio de calificaciones es {nota}")