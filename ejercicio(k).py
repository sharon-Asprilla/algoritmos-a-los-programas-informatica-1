print("Este programa (k) sirve para identificar los números primos de un intervalo")
print()

a = int(input("Ingrese el número a : "))
b = int(input("Ingrese el número b : "))

c = 1
divisores = 0 

inicial = a # guarda el valor de a inicial ya que cuando se hace el incremento con el contador a termina valiendo 
#21 cuando se pone a= 1 y b=20 por las veces quue conto el bucle del while, ya que dentro del while hay una variable a
# que imprime  esas veces 

while a <= b:
    while c <= a:
        if a % c == 0:
            divisores = divisores + 1
        c = c + 1
    if divisores == 2:
        print(a)
    
    a = a + 1
    divisores = 0
    c = 1

print("Los números primos entre", inicial, "y ",b,"son:")

