print("Este programa (L) imprime asteriscos alineados a la derecha")

n = int(input("Ingrese cuántas lineas quiere imprimir: "))

linea = 1

while linea <= n:
    espacios = n - linea
    if espacios >= 0:
        print(" " * espacios + "*" * linea)
    linea += 1
