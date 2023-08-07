# Lista de personas en la fila
fila = ["Juan", "María", "Pedro", "Ana", "Luis"]


def proceso_de_ingreso():
    # Ingreso de la primera persona en la fila
    persona_primero = fila.pop(0)
    print(f"{persona_primero} ingresa primero.")

    # Ingreso de la última persona en la fila
    persona_ultimo = fila.pop()
    print(f"{persona_ultimo} ingresa último.")


proceso_de_ingreso()

# Mostrar la fila después del proceso de ingreso
print("Personas en la fila después del ingreso:", fila)
