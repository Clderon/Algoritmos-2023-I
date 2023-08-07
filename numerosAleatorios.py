import random

# Definir las variables minimo, maximo y cantidad
minimo = int(
    input("Ingrese el valor mínimo del rango: ")
)  # Solicitar al usuario que ingrese el valor mínimo del rango
maximo = int(
    input("Ingrese el valor máximo del rango: ")
)  # Solicitar al usuario que ingrese el valor máximo del rango
cantidad = int(
    input("Ingrese la cantidad de números aleatorios a generar: ")
)  # Solicitar al usuario que ingrese la cantidad de números a generar

# Generar y mostrar los números aleatorios en el rango especificado
for i in range(cantidad):
    numeroAleatorio = random.randint(
        minimo, maximo
    )  # Generar un numero aleatorio entre el valor mínimo y máximo
    print(
        "Número aleatorio", i + 1, ":", numeroAleatorio
    )  # Mostrar el número aleatorio generado
