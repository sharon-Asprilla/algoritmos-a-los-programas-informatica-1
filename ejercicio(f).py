print("este programa (f) sirve para calcular los divisores de un numero ")
n = int(input("ingrese un numero: "))

x = 1

while x <= n:
    if n % x == 0:
        print(f"{x} es un divisor de {n}")
    x = x + 1
