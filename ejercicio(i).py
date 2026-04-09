print("programa (h) para calcular la serie de suma de números Fibonacci")
print("Ingresa cuántos números quieres ver de la serie:")
print()

n = int(input("Ingrese n: "))

a = 0
b = 1
contador = 0

print(" la serie es:")

while contador < n:
    c = a + b
    a = b
    b = c
    contador += 1
    print(a)
 
#aqui me falta repasar