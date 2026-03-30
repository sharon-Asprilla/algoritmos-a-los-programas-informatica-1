print("Algoritmo: imprimir pirámide de números")

n = int(input("Ingrese tamaño: "))

i = 1
while i <= n:
    t = 1
    linea = ""
    while t <= i:
        if t <= i:
            linea += str(t)
        t += 1
    print(linea)
    i += 1
