# Lista de calificaciones de los alumnos
calificaciones = [85, 92, 76, 60, 70, 95, 88, 50, 93, 80]

# Contar cuántos alumnos aprobaron el examen (calificación mayor o igual a 60)
aprobados = 0
for calificacion in calificaciones:
    if calificacion >= 60:
        aprobados += 1

# Contar cuántos alumnos obtuvieron una calificación sobresaliente (calificación mayor o igual a 90)
sobresalientes = calificaciones.count(95) + calificaciones.count(93)

print("Cantidad de alumnos que aprobaron:", aprobados)
print("Cantidad de alumnos con calificación sobresaliente:", sobresalientes)
