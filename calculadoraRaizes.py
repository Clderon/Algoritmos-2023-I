import math

# Solicitar al usuario que ingrese los coeficientes a, b y c
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4 * a * c

# Calcular las raíces de la ecuación cuadrática
if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    # Si el discriminante es mayor que cero, hay dos raíces reales diferentes
    print("Las raíces son:", raiz1, "y", raiz2)
elif discriminante == 0:
    raiz1 = -b / (2 * a)
    # Si el discriminante es igual a cero, hay una raíz doble
    print("La ecuación tiene una raíz doble:", raiz1)
else:
    # Si el discriminante es negativo, la ecuación no tiene raíces reales
    print("La ecuación no tiene raíces reales.")
