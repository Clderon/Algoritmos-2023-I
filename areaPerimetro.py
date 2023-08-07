import math


# Funciones para calcular el área y el perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# Funciones para calcular el área y el perímetro de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


# Funciones para calcular el área y el perímetro de un rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


print("1. Círculo")
print("2. Triángulo")
print("3. Rectángulo")
opcion = int(
    input(
        "Ingrese el número de la forma geométrica para calcular el área y el perímetro: "
    )
)

if opcion == 1:
    # Calcular el área y el perímetro de un círculo
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print("El área del círculo es:", area)
    print("El perímetro del círculo es:", perimetro)

elif opcion == 2:
    # Calcular el área y el perímetro de un triángulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    perimetro = calcular_perimetro_triangulo(base, lado1, lado2)
    print("El área del triángulo es:", area)
    print("El perímetro del triángulo es:", perimetro)

elif opcion == 3:
    # Calcular el área y el perímetro de un rectángulo
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = calcular_area_rectangulo(base, altura)
    perimetro = calcular_perimetro_rectangulo(base, altura)
    print("El área del rectángulo es:", area)
    print("El perímetro del rectángulo es:", perimetro)

else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
