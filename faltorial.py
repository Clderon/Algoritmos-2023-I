# Definir las variables resultado y numeroUsuario
resultado = 1
numeroUsuario = int(
    input("Ingrese un número: ")
)  # Solicitar al usuario que ingrese un numero

i = 1  # Inicializar la variable de iteración en 1

# Calcular el factorial del número ingresado mediante un bucle while
while i <= numeroUsuario:
    resultado = resultado * i  # Multiplicar el resultado por el valor actual de i
    i = i + 1  # Incrementar el valor de i en 1 para la siguiente iteración

# Mostrar el resultado del factorial en pantalla
print("El factorial de", numeroUsuario, "es:", resultado)
