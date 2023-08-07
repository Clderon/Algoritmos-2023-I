def es_primo(numero):
    contador = 0
    # Iterar desde 1 hasta el número (ambos inclusive)
    for i in range(1, numero + 1):
        # Si el número es divisible entre i, incrementar el contador
        if numero % i == 0:
            contador += 1

    # Un número primo solo tiene dos divisores: 1 y él mismo
    # Si el contador es igual a 2, entonces el número es primo
    if contador == 2:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")


# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es primo e imprimir el resultado
es_primo(numero)
