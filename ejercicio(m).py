print("este programa (m) sirve imprimir pirámide de números")

n = int(input("Ingrese tamaño: "))  # convierto el texto a número

i = 1
while i <= n:
    t = 1
    linea = ""
    # agrego espacios a la izquierda
    espacios = " " * (n - i)
    linea += espacios # es lo mismo que decir que  linea= linea + espacios 
    while t <= i:
        linea += str(t) + " " #aqui se convvierte el entero en un string
        t += 1
    print(linea)
    i += 1
