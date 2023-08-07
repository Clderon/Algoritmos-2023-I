def obtener_mayor(n):
    numeros = []  # Lista para almacenar los números ingresados

    # Solicitar al usuario que ingrese n números y guardarlos en la lista
    for i in range(n):
        numero = float(input("Ingrese el número " + str(i + 1) + ": "))
        numeros.append(numero)

    # Encontrar el número mayor en la lista utilizando la función max()
    mayor = max(numeros)

    return mayor


# Solicitar al usuario que ingrese la cantidad de números a comparar
cantidad_numeros = int(input("Ingrese la cantidad de números a comparar: "))

# Obtener el número mayor entre los números ingresados
mayor_numero = obtener_mayor(cantidad_numeros)

# Mostrar el número mayor encontrado en pantalla
print("El número mayor es:", mayor_numero)
