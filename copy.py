# Lista original de estudiantes
estudiantes = ["Juan", "María", "Luis", "Ana", "Pedro"]

# Hacemos una copia superficial de la lista de estudiantes
estudiantes_copia = estudiantes.copy()

# Agregamos un nuevo estudiante a la copia
nuevo_estudiante = "Laura"
estudiantes_copia.append(nuevo_estudiante)

# Eliminamos un estudiante de la copia
estudiante_eliminado = "María"
estudiantes_copia.remove(estudiante_eliminado)

# Mostramos ambas listas
print("Lista original de estudiantes:", estudiantes)
print("Copia de la lista de estudiantes:", estudiantes_copia)

