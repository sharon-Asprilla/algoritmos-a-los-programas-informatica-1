print("Algoritmo de suma de números Fibonacci")
print("Ingresa cuántos números quieres ver de la serie:")

n = int(input("Ingrese n: "))

a = 0
b = 1
contador = 0

while contador < n:
    print("El número de la serie es:", a)
    c = a + b
    a = b
    b = c
    contador += 1
 
