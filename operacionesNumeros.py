def realizar_operacion(opcion, num1, num2):
    # Realizar la operación correspondiente según la opción elegida
    if opcion == 1:
        return num1 + num2
    elif opcion == 2:
        return num1 - num2
    elif opcion == 3:
        return num1 * num2
    elif opcion == 4:
        # Verificar si se puede realizar la división entre num1 y num2
        if num2 == 0:
            return "No se puede dividir entre cero."
        else:
            return num1 / num2
    else:
        return "Opción inválida."


# Solicitar al usuario que ingrese los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar las opciones de operaciones matemáticas
print("\nOpciones de operaciones matemáticas:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División\n")

# Solicitar al usuario que ingrese la opcion deseada
opcion = int(input("Ingrese el número de la opción deseada: "))

# Realizar la operacion y obtener el resultado
resultado = realizar_operacion(opcion, num1, num2)

# Mostrar el resultado en pantalla
print("El resultado es:", resultado)
