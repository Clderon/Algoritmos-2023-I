# Lista de números
numeros = [2, 5, 3, 7, 4, 5, 9]

# Número que queremos eliminar de la lista
numero_a_eliminar = 5


def eliminar_primera_aparicion(lista, numero):
    if numero in lista:
        lista.remove(numero)
        print("Se eliminó la primera aparición del número ", numero, " en la lista.")
    else:
        print("El número ", numero, " no está presente en la lista.")


eliminar_primera_aparicion(numeros, numero_a_eliminar)

print("Lista después de eliminar el número:", numeros)
