def es_primo(numero):
    contador = 0
    # Iterar desde 1 hasta el numero (ambos inclusive)
    for i in range(1, numero + 1):
        # Si el número es divisible entre i, incrementar el contador
        if numero % i == 0:
            contador += 1

    # Un numero primo solo tiene dos divisores: 1 y el mismo
    # Si el contador es igual a 2, entonces el numero es primo
    if contador == 2:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")


# Solicitar al usuario que ingrese un numero
numero = int(input("Ingrese un número: "))

# Verificar si el numero es primo e imprimir el resultado
es_primo(numero)
