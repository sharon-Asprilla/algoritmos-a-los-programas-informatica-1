print("programa (b) para calcular las cordenadas")
print()
x1 = int(input("ingrese el x1: "))
y1 = int(input("ingrese el y1: "))
x2 = int(input("ingrese el x2: "))
y2 = int(input("ingrese el y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #eleva al cuadrado todas las potencias que se hacen a los puntos,
#0.5 es igual a sacar la raiz,se pone dos ** para hacer la potencia
print("la distancia de los numeros ingresados es: ",distancia)

