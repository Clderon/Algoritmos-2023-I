def mostrar_estacion(numero_mes):
    # Mostrar la estación correspondiente segun el numero del mes
    if numero_mes == 1 or numero_mes == 2 or numero_mes == 12:
        print("La estación correspondiente es: Verano")
    elif numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
        print("La estación correspondiente es: Otoño")
    elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
        print("La estación correspondiente es: Invierno")
    elif numero_mes == 9 or numero_mes == 10 or numero_mes == 11:
        print("La estación correspondiente es: Primavera")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 12.")


# Solicitar al usuario que ingrese un numero del 1 al 12
numero_mes = int(input("Ingrese un número del 1 al 12: "))

# Llamar a la función para mostrar la estacion correspondiente
mostrar_estacion(numero_mes)
