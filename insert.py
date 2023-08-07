calificaciones = [85, 78, 92, 80, 88]

# Obtener la nueva calificación del estudiante 
nueva_calificacion = int(input("Ingresa una nueva calificacion: "))

# Si la calificación es mayor que 90, insertarla al principio de la lista; 
# de lo contrario, insertarla al final
if nueva_calificacion > 90:
    calificaciones.insert(0, nueva_calificacion)
else:
    calificaciones.append(nueva_calificacion)

print("Calificaciones de los estudiantes:", calificaciones)
