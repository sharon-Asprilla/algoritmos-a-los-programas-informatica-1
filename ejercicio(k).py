print("Este algoritmo sirve para identificar los números primos de un intervalo")
print()

a = int(input("Ingrese el número a : "))
b = int(input("Ingrese el número b : "))

c = 1
divisores = 0 



while a <= b:
    while c < a:
        if a % c == 0:
            divisores = divisores + 1
        c = c + 1
    if divisores == 2:
        print(a)
    
    a = a + 1
    divisores = 0
    c = 1

print(f"Los números primos entre {a} y {b} son:")

