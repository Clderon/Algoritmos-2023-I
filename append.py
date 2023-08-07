# Lista de números
numeros = [2, 7, 15, 10, 8, 3, 6]

# Listas para números pares e impares
numeros_pares = []
numeros_impares = []

# Iterar sobre la lista de números
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Mostrar los resultados
print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)
