import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo")
    return math.sqrt(a)

def seno(angulo_grados):
    return math.sin(math.radians(angulo_grados))

if __name__ == "__main__":
    print("Calculadora Científica")
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"Raíz de 16 = {raiz_cuadrada(16)}")
    print(f"Seno de 90° = {seno(90)}")