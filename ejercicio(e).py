print("Algoritmo de menú de opciones")
print()

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))   

opcion = 0

while opcion != 5:
    print("1. Multiplicación")
    print("2. Residuo")
    print("3. Potencia")
    print("4. Comparación")
    print("5. Salir")
    opcion = int(input("Ingrese la opción: "))

    if opcion == 1: 
        resultado = a * b
        print("El resultado es:", resultado)
        print("**************************")
    elif opcion == 2:
        residuo = a % b
        print("El residuo es:", residuo) 
        print("**************************")
    elif opcion == 3:
        potencia = a ** b   #dos ** para hacer potencia
        print("La potencia es:", potencia)
        print("**************************")
    elif opcion == 4:
        if a > b:
            print(f"{a} es mayor que {b}")
        elif a < b:
            print(f"{b} es mayor que {a}")
        else:
            print(f"{a} es igual a {b}")
        print("**************************")
    elif opcion == 5:
        print("Salir")
        print("**************************")
